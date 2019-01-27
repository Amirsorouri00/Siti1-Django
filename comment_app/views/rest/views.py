import datetime
from rest_framework import viewsets
from fluent_comments.models import FluentComment
from comment_app.serializers.comment_serializer import CommentSerializer
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework import status


class CommentViewSet(viewsets.ModelViewSet):
    queryset = FluentComment.objects.all()
    serializer_class = CommentSerializer
    def create(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        if True:
            data = self.request.data
            comment = data.get('comment')
            if comment is None:
                return Response('comment is None', status=status.HTTP_412_PRECONDITION_FAILED)    
            news = data['News']
            if 'parent' in data:
                parent = data['parent']
            else:
                parent = None
            submit_date = datetime.datetime.now()
            content = ContentType.objects.get(model="news").pk
            # comment = FluentComment.objects.create(object_pk=news, comment=comment, submit_date=submit_date, content_type_id=content, user_id = self.request.user.id, site_id=settings.SITE_ID, parent_id=parent)
            comment = FluentComment.objects.create(object_pk=news, comment=comment, submit_date=submit_date, content_type_id=content, user_id = 1, site_id=settings.SITE_ID, parent_id=parent)
            serializer = CommentSerializer(comment,context=  {'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)