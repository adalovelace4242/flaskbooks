import os
from concurrent import futures
import random

import grpc

from data import books_by_category
from recommendations_pb2 import (
    RecommendationResponse, RecommendationRequest,
)
import recommendations_pb2_grpc


grpc_port = os.getenv("GRPC_PORT", "50051")


class RecommendationService(
    recommendations_pb2_grpc.RecommendationsServicer
):
    def Recommend(self, request: RecommendationRequest, context: grpc.ServicerContext):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        books_for_result = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_result))
        books_to_recommend = random.sample(books_for_result, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)


def serve():
    threadpool = futures.ThreadPoolExecutor(max_workers=10)
    server = grpc.server(threadpool)
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(RecommendationService(), server)
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()
    print("Recommendation server is running!")
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting Recommendation ...")
    serve()
