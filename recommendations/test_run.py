from recommendations.recommendations import RecommendationService
from recommendations_pb2 import RecommendationRequest, BookCategory
from recommendations_pb2_grpc import RecommendationsStub


def test_recommendations():
    service = RecommendationService()
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=1
    )
    response = service.Recommend(request, None)
    assert len(response.recommendations) == 1


if __name__ == '__main__':
    import grpc

    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)
    request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
    result = client.Recommend(request)
    print(result)

