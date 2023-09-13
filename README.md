# Key-value store client

Implementation of a KVS client according to specifications [here](https://paulo-coelho.github.io/ds_notes/projeto/).

## Compilation

Run `./compile.sh`

Python 3 is required.

## Usage

* Run one of the following (use `-h` to see available arguments):

`./client.sh <arg1> <arg2> ... <argn>`

`source bin/activate && ./kvs_client.py <arg1> <arg2> ... <argn>`

## Examples and expected output

```bash
# operations, port and arguments
./client.sh -h
usage: kvs_client [-h] [--port PORT] --op {get,getrange,getall,put,putall,del,delrange,delall,trim} --key KEY [KEY ...]
                  [--val VAL [VAL ...]] [--ver VER [VER ...]]

Key-value store client

options:
  -h, --help            show this help message and exit
  --port PORT           server port
  --op {get,getrange,getall,put,putall,del,delrange,delall,trim}
                        the operation to perform on the server
  --key KEY [KEY ...]   one or more keys, depending on the operation
  --val VAL [VAL ...]   one or more values, depending on the operation
  --ver VER [VER ...]   one or more versions, depending on the operation

# non-existing key
./client.sh --op get --key xxx
args = Namespace(port=50051, op='get', key=['xxx'], val=None, ver=None)
Response = key: "xxx"

# inserting multiple keys and values
./client.sh --op putall --key abc k1 k2 k22 k111 k5 k20 --val zyx asf gdfg hgfhf adas bcvbcv uyiuy
args = Namespace(port=50051, op='putall', key=['abc', 'k1', 'k2', 'k22', 'k111', 'k5', 'k20'], val=['zyx', 'asf', 'gdfg', 'hgfhf', 'adas', 'bcvbcv', 'uyiuy'], ver=None)
Response = [key: "abc"
ver: 1694605431790
, key: "k1"
ver: 1694605431790
, key: "k2"
ver: 1694605431790
, key: "k22"
ver: 1694605431790
, key: "k111"
ver: 1694605431791
, key: "k5"
ver: 1694605431791
, key: "k20"
ver: 1694605431791
]

# get valid key, no version
./client.sh --op get --key abc
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=None)
Response = key: "abc"
val: "zyx"
ver: 1694605431790

# insert new value for existing key
./client.sh --op put --key abc --val bbbccc
args = Namespace(port=50051, op='put', key=['abc'], val=['bbbccc'], ver=None)
Response = key: "abc"
old_val: "zyx"
old_ver: 1694605431790
ver: 1694605550466

# get existing key with latest version
./client.sh --op get --key abc --ver 0
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=[0])
Response = key: "abc"
val: "bbbccc"
ver: 1694605550466

# get existing key with a too old version
./client.sh --op get --key abc --ver 1
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=[1])
Response = key: "abc"
ver: 1

# get existing key with an exact previous version
./client.sh --op get --key abc --ver 1694605431790
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=[1694605431790])
Response = key: "abc"
val: "zyx"
ver: 1694605431790

# get existing key with a previous version
./client.sh --op get --key abc --ver 1694605431791
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=[1694605431791])
Response = key: "abc"
val: "zyx"
ver: 1694605431790

# get existing key with current version
./client.sh --op get --key abc --ver 1694605550466
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=[1694605550466])
Response = key: "abc"
val: "bbbccc"
ver: 1694605550466

# get existing key with version greater than current version
./client.sh --op get --key abc --ver 1694605550999
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=[1694605550999])
Response = key: "abc"
val: "bbbccc"
ver: 1694605550466

# get a key range (respects alphabetical order)
./client.sh --op getrange --key a k
args = Namespace(port=50051, op='getrange', key=['a', 'k'], val=None, ver=None)
Response = [key: "abc"
val: "bbbccc"
ver: 1694605550466
]

# get a key range (respects alphabetical order)
./client.sh --op getrange --key a k2
args = Namespace(port=50051, op='getrange', key=['a', 'k2'], val=None, ver=None)
Response = [key: "abc"
val: "bbbccc"
ver: 1694605550466
, key: "k1"
val: "asf"
ver: 1694605431790
, key: "k111"
val: "adas"
ver: 1694605431791
, key: "k2"
val: "gdfg"
ver: 1694605431790
]

# get a key range (respects alphabetical order)
./client.sh --op getrange --key a k12
args = Namespace(port=50051, op='getrange', key=['a', 'k12'], val=None, ver=None)
Response = [key: "abc"
val: "bbbccc"
ver: 1694605550466
, key: "k1"
val: "asf"
ver: 1694605431790
, key: "k111"
val: "adas"
ver: 1694605431791
]

# get a key range (respects alphabetical order) with version
./client.sh --op getrange --key a k12 --ver 1 1
args = Namespace(port=50051, op='getrange', key=['a', 'k12'], val=None, ver=[1, 1])
Response = [key: "abc"
ver: 1
, key: "k1"
ver: 1
, key: "k111"
ver: 1
]

# get a key range (respects alphabetical order) with version
./client.sh --op getrange --key a k12 --ver 1694605431790 1694605431790
args = Namespace(port=50051, op='getrange', key=['a', 'k12'], val=None, ver=[1694605431790, 1694605431790])
Response = [key: "abc"
val: "zyx"
ver: 1694605431790
, key: "k1"
val: "asf"
ver: 1694605431790
, key: "k111"
ver: 1694605431790
]

# get a key range (respects alphabetical order) with version (greatest version must be used)
./client.sh --op getrange --key a k12 --ver 1694605431790 1694605999999
args = Namespace(port=50051, op='getrange', key=['a', 'k12'], val=None, ver=[1694605431790, 1694605999999])
Response = [key: "abc"
val: "bbbccc"
ver: 1694605550466
, key: "k1"
val: "asf"
ver: 1694605431790
, key: "k111"
val: "adas"
ver: 1694605431791
]

# get multiple keys (existing and non-existing)
./client.sh --op getall --key k2 k11 k111
args = Namespace(port=50051, op='getall', key=['k2', 'k11', 'k111'], val=None, ver=None)
Response = [key: "k2"
val: "gdfg"
ver: 1694605431790
, key: "k11"
, key: "k111"
val: "adas"
ver: 1694605431791
]

# delete a key
 ./client.sh --op del --key k1
args = Namespace(port=50051, op='del', key=['k1'], val=None, ver=None)
Response = key: "k1"
val: "asf"
ver: 1694605431790

# delete a key range
./client.sh --op delrange --key k2 k22
args = Namespace(port=50051, op='delrange', key=['k2', 'k22'], val=None, ver=None)
Response = [key: "k2"
val: "gdfg"
ver: 1694605431790
, key: "k20"
val: "uyiuy"
ver: 1694605431791
, key: "k22"
val: "hgfhf"
ver: 1694605431790
]

# delete multiple keys (existing and non-existing)
./client.sh --op delall --key k111 k333 k5
args = Namespace(port=50051, op='delall', key=['k111', 'k333', 'k5'], val=None, ver=None)
Response = [key: "k111"
val: "adas"
ver: 1694605431791
, key: "k333"
, key: "k5"
val: "bcvbcv"
ver: 1694605431791
]

# trim key 'abc' (value is 'zyx' for version 1694605431790 and 'bbbccc' for version 1694605550466)
./client.sh --op trim --key abc
args = Namespace(port=50051, op='trim', key=['abc'], val=None, ver=None)
Response = key: "abc"
val: "bbbccc"
ver: 1694605550466

# get old value for key 'abc' after trim
./client.sh --op get --key abc --ver 1694605431790
args = Namespace(port=50051, op='get', key=['abc'], val=None, ver=[1694605550461])
Response = key: "abc"
ver: 1694605431790
```
