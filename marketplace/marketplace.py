import os

import grpc
from flask import Flask, render_template

from recommendations_pb2 import RecommendationRequest, BookCategory
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
grpc_port = os.getenv("GRPC_PORT", "50051")
recommendations_channel = grpc.insecure_channel(f'{recommendations_host}:{grpc_port}')
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route('/')
def render_homepage():
    request = RecommendationRequest(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    response = recommendations_client.Recommend(request)
    return render_template("homepage.html", recommendations=response.recommendations)


if __name__ == '__main__':
    app.run()
