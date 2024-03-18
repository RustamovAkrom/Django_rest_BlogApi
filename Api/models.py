from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class User(AbstractUser):
    birthday = models.DateField(null = True, blank = True)
    bio = models.TextField(null = True, blank = True)

    def __str__(self): return self.username


class Post(AbstractBaseModel):
    title = models.CharField(max_length = 128)
    body = models.TextField()
    is_active = models.BooleanField(default = False)
    authors = models.ForeignKey(User, models.CASCADE, 'posts')

    class Meta:
        db_table = 'posts'

    @property
    def like_count(self): self.likes.count()

    def __str__(self): return self.title


class Comment(AbstractBaseModel):
    body = models.TextField()
    authors = models.ForeignKey(User, models.CASCADE, 'comments')
    posts = models.ForeignKey(Post, models.CASCADE, 'comments')

    class Meta:
        db_table = 'comments'

    def __str__(self): return f"{self.authors} --> {self.posts}"


class Like(AbstractBaseModel):
    authors = models.ForeignKey(User, DO_NOTHING, 'likes')
    posts = models.ForeignKey(Post, models.CASCADE, 'likes')

    class Meta:
        db_table = 'post_likes'

    def __str__(self): return f"{self.authors} -like-> {self.posts}"
