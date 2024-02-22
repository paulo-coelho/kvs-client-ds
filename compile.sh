#!/bin/bash

pipenv shell

pip install -r requirements.txt

python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I./proto proto/pa.proto
python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I./proto proto/pm.proto
