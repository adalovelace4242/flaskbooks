#!/bin/bash

set -e

#venv3/Scripts/activate.bat
python -m grpc_tools.protoc -I ../protobufs --python_out=.    --grpc_python_out=.   --mypy_out=. ../protobufs/recommendations.proto ../protobufs/recommendations.proto
python recommendations.py

