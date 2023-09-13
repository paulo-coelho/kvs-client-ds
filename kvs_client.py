#!/usr/bin/env python3
"""kvs grpc client"""

import argparse
import sys

import grpc
import kvs_pb2
import kvs_pb2_grpc


def key_request(k, v=None):
    '''returns the correct object for a key and version parameter'''
    return kvs_pb2.KeyRequest(key=k, ver=v)


def key_range(f, t, fv=0, tv=0):
    '''returns the correct object for the key interval'''
    fr = kvs_pb2.KeyRequest(key=f, ver=fv)
    to = kvs_pb2.KeyRequest(key=t, ver=tv)
    return kvs_pb2.KeyRange(fr=fr, to=to)


def put_request(k, v):
    '''returns the correct object for a key and value parameter'''
    return kvs_pb2.KeyValueVersionReply(key=k, val=v)


def putall_request(k, v):
    '''returns the correct object for a  key-value array parameter'''
    if len(k) != len(v):
        print("The number of keys and values must be the same")
        sys.exit(1)
    for i in range(0, len(k)):
        yield put_request(k[i], v[i])


def getall_request(k, v):
    '''returns the correct object for a key/version array parameter'''
    if v is not None and len(k) != len(v):
        print("The number of keys and values must be the same")
        sys.exit(1)
    for i in range(0, len(k)):
        yield key_request(k[i], 0 if v is None else v[i])


# command line arguments
def set_args():
    parser = argparse.ArgumentParser(prog='kvs_client',
                                     description='Key-value store client')
    parser.add_argument("--port", default=50051, type=int, help="server port")
    parser.add_argument("--op",
                        choices=[
                            "get",
                            "getrange",
                            "getall",
                            "put",
                            "putall",
                            "del",
                            "delrange",
                            "delall",
                            "trim",
                        ],
                        required=True,
                        help="the operation to perform on the server")
    parser.add_argument("--key",
                        nargs="+",
                        required=True,
                        help="one or more keys, depending on the operation")
    parser.add_argument("--val",
                        nargs="+",
                        help="one or more values, depending on the operation")
    parser.add_argument(
        "--ver",
        nargs="+",
        type=int,
        help="one or more versions, depending on the operation")
    return parser


def main():
    """main function"""
    args = set_args().parse_args()
    port = args.port or 50051
    with grpc.insecure_channel(f"127.0.0.1:{port}") as channel:
        print(f"args = {args}")
        stub = kvs_pb2_grpc.KeyValueStoreStub(channel)

        if args.op == "get":
            ver = args.ver or [0]
            res = stub.Get(key_request(args.key[0], ver[0]))
        elif args.op == "getrange":
            if len(args.key) != 2:
                print("Informe apenas duas chaves")
                sys.exit(1)
            f = args.key[0]
            t = args.key[1]
            fv = 0 if args.ver is None or len(args.ver) != 2 else args.ver[0]
            tv = 0 if args.ver is None or len(args.ver) != 2 else args.ver[1]
            res = []
            for r in stub.GetRange(key_range(f, t, fv, tv)):
                res.append(r)
        elif args.op == "getall":
            r_it = getall_request(args.key, None)
            res = []
            for r in stub.GetAll(r_it):
                res.append(r)
        elif args.op == "put":
            res = stub.Put(put_request(args.key[0], args.val[0]))
        elif args.op == "putall":
            r_it = putall_request(args.key, args.val)
            res = []
            for r in stub.PutAll(r_it):
                res.append(r)
        elif args.op == "del":
            res = stub.Del(key_request(args.key[0]))
        elif args.op == "delrange":
            if len(args.key) != 2:
                print("Informe apenas duas chaves")
                sys.exit(1)
            f = args.key[0]
            t = args.key[1]
            res = []
            for r in stub.DelRange(key_range(f, t)):
                res.append(r)
        elif args.op == "delall":
            r_it = getall_request(args.key, None)
            res = []
            for r in stub.DelAll(r_it):
                res.append(r)
        elif args.op == "trim":
            res = stub.Trim(key_request(args.key[0]))

        print(f"Response = {res}")


if __name__ == "__main__":
    main()
