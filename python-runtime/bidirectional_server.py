from concurrent import futures
import json

import grpc
import bidirectional_pb2_grpc as bidirectional_pb2_grpc
import logging
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



class BidirectionalService(bidirectional_pb2_grpc.BidirectionalServicer):

    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            logging.info(f'Received message: {message}')
            message.message = get_trending_repos()
            print(type(message))
            yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bidirectional_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


# call https://gh-trending-api.herokuapp.com/repositories api to get trending repos
def get_trending_repos():
    url = "https://gh-trending-api.herokuapp.com/repositories"
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    serve()