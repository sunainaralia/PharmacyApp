from rest_framework import serializers
from .models import Rating


# serializer for rating
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
