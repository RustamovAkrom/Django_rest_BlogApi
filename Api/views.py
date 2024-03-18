from django.shortcuts import render, get_object_or_404
from Api.models import User, Post, Comment, Like

from Api.permisions import IsSuperUser, IsStaffPermission, IsOwner

from Api.serializers import (UserSerializer, UserListSerializer,
                             PostSerializer, CommentSerializer,
                             CommentListSerializer, LikeSerializer,
                             LikeListSerializer, PostDetailSerializer,
                             PostListSerializer, TopPostSerializer)

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.decorators import action
from django.db.models import Q


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsSuperUser, IsOwner, ]

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(data = {"detail": "User registered"}, status = status.HTTP_201_CREATED)

    def list(self, request):
        queryset = User.objects.all()

        serializer = UserListSerializer(instance = queryset, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsStaffPermission, IsOwner, ]
    
    #searching
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "title":['icontains', 'startswith'],
        "body":['icontains',  ],
        # "comments": ['icontains', ]
    }

    @action(detail = True, methods = ['post'], url_path = 'press-like')
    def Like_post(self, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        like = Like.objects.create(posts = post, authors = user)
        serializer = LikeSerializer(like)
        return Response(data = serializer.data, status = status.HTTP_201_CREATED)

    @action(detail = True, methods = ['post'], url_path = 'press-dislike')
    def dislike_post(self, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        like = Like.objects.get(posts = post, authors = user)
        like = get_object_or_404(Like, author=user, posts=post)
        like.delete()
        return Response(data = {"data": "User deleted"}, status = status.HTTP_200_OK)

    @action(detail = False, methods = ['get'], url_path = 'top_posts')
    def top_posts(self, *args, **kwargs):
        post = self.get_queryset().order_by('likes')[:3]
        # output = []
        # ls = [(obj, len(obj.likes.all())) for obj in post]
        # for i in ls:
        #     print(i[1])
        serializer = TopPostSerializer(post, many = True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['get'], url_path='ordering_id')
    def ordering_id(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(instance=queryset.order_by('-id'), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    
    # def get_queryset(self):
    #     posts = self.queryset
    #     search = self.request.query_params
    #     try:
    #         title = search['title']
    #         body = search['body']
    #         queryset = posts.filter(
    #             title__icontains = title, body__icontains = body)
    #         # queryset.order_by('id')
    #         # queryset.order_by('like_count')
    #         return queryset
    #     except:
    #         return posts
        
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(data = {"detail": "Post created"}, status = status.HTTP_201_CREATED)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostListSerializer(instance = queryset, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        # print(request.user.auth_token)
        queryset = get_object_or_404(Post, pk = pk)
        serializer = PostDetailSerializer(instance = queryset)
        return Response(data = serializer.data, status = status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(data = {"detail": f"Add comment "})

    def list(self, request, *args, **kwargs):
        queryset = Comment.objects.all().select_related('authors', 'posts')
        serializer = CommentListSerializer(instance = queryset, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)



class LikeViewSet(ViewSet):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = LikeSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(data = {"detail": "Like Button 👍"})

    def list(self, request, *args, **kwargs):
        queryset = Like.objects.all()
        serializer = LikeListSerializer(instance = queryset, many = True)
        return Response(data = serializer.data, status = status.HTTP_200_OK)


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_202_ACCEPTED)