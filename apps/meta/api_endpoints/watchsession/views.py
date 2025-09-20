from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from apps.meta.api_endpoints.watchsession.serializers import WatchSessionCreateSerializer

class WatchSessionCreateView(APIView):
    def post(self, request, pk):
        data = request.data.copy()
        data['movie'] = pk  
        serializer = WatchSessionCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'ok'})

class WatchSessionCreateView(CreateAPIView):
    serializer_class = WatchSessionCreateSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        serializer.save(movie_id=pk)
