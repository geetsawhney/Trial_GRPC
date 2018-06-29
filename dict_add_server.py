
from concurrent import futures
import time

import grpc

import dict_add_pb2
import dict_add_pb2_grpc
from google.protobuf import struct_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DictAddServicer(dict_add_pb2_grpc.DictAddServicer):

    def Add_Dict(self, request, context):
        print(context)
        server_dict=dict(request.s)
        print(server_dict)
        server_dict['owner']= 1.11001
        st=struct_pb2.Struct()
        for key in server_dict.iterkeys():
            st[key]=server_dict[key]
        return dict_add_pb2.Dict(s=st)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dict_add_pb2_grpc.add_DictAddServicer_to_server(DictAddServicer(), server)
    server.add_insecure_port('[::]:50003')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
