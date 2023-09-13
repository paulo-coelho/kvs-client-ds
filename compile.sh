#!/bin/bash


python3 -m venv .
source bin/activate 

pip install -r requirements.txt

python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I./proto proto/kvs.proto
