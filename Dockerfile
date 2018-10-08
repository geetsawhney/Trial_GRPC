FROM grpc/python:1.0-onbuild
EXPOSE 50051
CMD [ "python", "./dict_add_server.py" ]
