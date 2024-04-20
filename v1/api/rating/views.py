from .models import Rating
from .serializers import RatingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from v1.renderers import ErrorRenderer


# VIEW FOR POST VIEW
class RatingView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request, format=None):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"msg": "rating is saved successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
