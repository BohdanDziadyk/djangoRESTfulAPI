from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import UserModel, PostModel, CommentModel
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserLCView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class PostLCView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()


class PostRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()


class CommentLCView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()


class CommentRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()
