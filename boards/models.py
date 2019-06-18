from django.db import models
from django.conf import settings


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 게시물에 user를 붙여주는 코드, CASCADE => 유저 삭제시 게시글을 같이 삭제하라
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)