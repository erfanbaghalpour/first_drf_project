from rest_framework import serializers
from blog.models import Article


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

class ArticleSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(write_only=True)

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

    # def validate_title(self, value):
    #     if value == "html":
    #         raise serializers.ValidationError("You can choose html")
    #     return value
    # def validate(self, attrs):
    #     if attrs['title'] == attrs['text']:
    #         raise serializers.ValidationError("title and text can not be the same!")
    #     return attrs
