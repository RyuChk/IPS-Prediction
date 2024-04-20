import handlers.prediction as handlers
from concurrent import futures
from dotenv import load_dotenv
import ips.model.v1.model_pb2_grpc as modelv1_grpc
import os

import grpc

load_dotenv()
server_port = os.getenv("APP_PORT")
if not server_port:
    server_port = 8080

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    modelv1_grpc.add_ModelServiceServicer_to_server(handlers.ModelServiceServicer(), server)
    server.add_insecure_port(f"[::]:{server_port}")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print(f"Serving prediction service at port [::]:{server_port}")
    serve()