from rest_framework import serializers
from file_app.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('uuid', 'file', 'remark', 'file_category', 'timestamp')
        read_only_fields = ('id', 'uuid', 'timestamp')