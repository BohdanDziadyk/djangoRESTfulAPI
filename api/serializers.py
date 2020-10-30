from rest_framework.serializers import ModelSerializer

from .models import UserModel, PostModel, CommentModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'
