from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=190)


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()
    status = serializers.BooleanField()