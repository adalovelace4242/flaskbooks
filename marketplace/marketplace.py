import os

from grpc import insecure_channel
from flask import Flask, render_template

# todo: try use https://grpc.github.io/grpc/python/grpc.html#runtime-protobuf-parsing
from recommendations_pb2 import RecommendationRequest, BookCategory
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
grpc_port = os.getenv("GRPC_PORT", "50051")
recommendations_channel = insecure_channel(f'{recommendations_host}:{grpc_port}')
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route('/')
def render_homepage():
    request = RecommendationRequest(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    response = recommendations_client.Recommend(request)
    return render_template("homepage.html", recommendations=response.recommendations)


if __name__ == '__main__':
    app.run()
