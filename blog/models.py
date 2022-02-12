from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone # django で日付を管理するためのモジュール
from django.contrib.auth import  get_user_model

class User(AbstractUser):
    email = models.EmailField('メールアドレス',unique=True)

class Article(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self): # Post モデルが直接呼び出された時に返す値を定義
        return self.title # 記事タイトルを返す
