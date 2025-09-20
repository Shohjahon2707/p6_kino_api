from rest_framework import serializers
from apps.meta.models import Like

class MovieLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
    
__all__=["MovieLikeSerializer"]