import datetime
from rest_framework import status
from comment_app.models import News
from rest_framework import viewsets
from rest_framework.response import Response
from comment_app.serializers.news_serializer import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def retrieve(self, request, pk=None):
        news = self.get_object(pk)
        serializer = self.serializer_class(news,context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()