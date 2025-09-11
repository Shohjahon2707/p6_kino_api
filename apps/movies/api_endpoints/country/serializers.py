from rest_framework import serializers

from apps.movies.models import Country

class MovieCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model=Country
        fields = ["id",'name']

__all__=["MovieCountrySerializer"]