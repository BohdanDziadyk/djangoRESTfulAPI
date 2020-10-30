from django.urls import path

from .views import UserLCView, UserRUDView, PostLCView, PostRUDView, CommentLCView, CommentRUDView

urlpatterns = [
    path('users/', UserLCView.as_view()),
    path('users/<int:pk>', UserRUDView.as_view()),
    path('posts/', PostLCView.as_view()),
    path('posts/<int:pk>', PostRUDView.as_view()),
    path('comments/', CommentLCView.as_view()),
    path('comments/<int:pk>', CommentRUDView.as_view())
]
