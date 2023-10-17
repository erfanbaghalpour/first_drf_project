from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from persiantools.jdatetime import JalaliDate

from blog.models import Article, Comment


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=190)


def check_title(attrs):
    if attrs['title'] == "html":
        raise serializers.ValidationError({"title": "title can not be html"})


class CheckTitle:
    def __call__(self, attrs):
        if attrs["title"] == 'html':
            raise serializers.ValidationError({"title": "title can not be html"})


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(validators=[CheckTitle()])
#     text = serializers.CharField()
#     status = serializers.BooleanField(required=False)
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    days_ago = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_days_ago(self, obj):
        return (now().date() - obj.date).days

    def get_date(self, obj):
        date = JalaliDate(obj.date, locale="fa")
        return date.strftime('%c')


class ArticleSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(write_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ("__all__")
        validators = [
            CheckTitle()
        ]
        # also we can filter them by using the codes in below :
        # fields = ("title", "text", ...)
        # and if we want to remove a field we can use this :
        # exclude = ("status", ...)

        read_only_fields = ["id"]

    def get_comments(self, obj):
        serializer = CommentSerializer(instance=obj.comments.all(), many=True)
        return serializer.data

# def validate_title(self, value):
#     if value == "html":
#         raise serializers.ValidationError("You can choose html")
#     return value
# def validate(self, attrs):
#     if attrs['title'] == attrs['text']:
#         raise serializers.ValidationError("title and text can not be the same!")
#     return attrs
