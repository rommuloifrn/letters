import grpc
import correio_pb2
import correio_pb2_grpc
from concurrent import futures

class CorreioServicer(correio_pb2_grpc.CorreioServicer):

    cartas = ['pequende']

    def SendCartas(self, request, context):
        carta = request.texto
        self.cartas.append(carta)
        return "foda"
    def GetCartas(self, request, context):
        return self.cartas
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    correio_pb2_grpc.add_CorreioServicer_to_server(CorreioServicer(), server)
    server.add_insecure_port("[::]:8080")
    server.start()
    server.wait_for_termination()

print("imma try bootin....")

try:
    serve()
except:
    print("fuck. cant do eit.")
