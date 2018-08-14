"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import time

import grpc

from proto import dict_add_pb2
from proto import dict_add_pb2_grpc
from google.protobuf import struct_pb2

avaluo = {'origin': 'Google','banos':None, 'floors': 1}

st=struct_pb2.Struct()
for key in avaluo.keys():
    st[key]=avaluo[key]

channel = grpc.insecure_channel('localhost:50003')
stub = dict_add_pb2_grpc.DictAddStub(channel)
response = stub.Add_Dict(dict_add_pb2.Dict(s=st))
print(dict(response.s))
