# from rest_framework.routers import DefaultRouter
# from Api.views import UserViewSet, PostViewSet, CommentViewSet, LikeViewSet
# router = DefaultRouter()

# router.register('users', UserViewSet, 'user')
# router.register('posts', PostViewSet, 'post')
# router.register('likes', LikeViewSet, 'like')
# router.register('comments', CommentViewSet, 'comment')


from api_endpoints.Comment import *
from api_endpoints.Like import *
from api_endpoints.Post import *
from api_endpoints.User import *

from django.urls import path, include
from rest_framework.authtoken import views
from Api.views import Logout

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),

    path('comment-list/', CommentListAPIView.as_view()),
    path('comment-create/', CommentCreateAPIView.as_view()),
    path('comment-destroy/<pk>', CommentDestroyAPIView.as_view()),
    path('comment-retrive/<pk>', CommentRetriveAPIView.as_view()),
    path('comment-update/<pk>', CommentUpdateAPIView.as_view()),

    path('like-create/', LikeCreateAPIView.as_view()),
    path('like-destroy/<pk>', LikeDestroyAPIView.as_view()),
    path('like-list/', LikeListAPIView.as_view()),
    path('like-retrive/<pk>', LikeRetriveAPIView.as_view()),
    path('like-update/<pk>', LikeUpdateAPIView.as_view()),

    path('post-create/', PostCreateAPIView.as_view()),
    path('post-destroy/<pk>', PostDestroyAPIView.as_view()),
    path('post-list/', PostListAPIView.as_view()),
    path('post-retrive/<pk>', PostRetriveAPIView.as_view()),
    path('post-update/<pk>', PostUpdateAPIView.as_view()),

    path('user-create', UserCreateAPIView.as_view()),
    path('user-destroy/<pk>', UserDestroyAPIView.as_view()),
    path('user-list/', UserListAPIView.as_view()),
    path('user-retrive/<pk>', UserRetriveAPIView.as_view()),
    path('user-update/<pk>', UserUpdateAPIView.as_view())

]
