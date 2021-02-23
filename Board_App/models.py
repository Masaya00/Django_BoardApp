from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50)
    # 必須 / デフォルトに現在日時を指定
    created_at = models.DateTimeField('登録日時', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'スレッド'
        verbose_name_plural = 'スレッド'

class Comment(models.Model):
    # スレッドにコメントを紐付け。　スレッドが削除されればコメントも削除
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    # 必須 / デフォルトに現在日時を指定
    created_at = models.DateTimeField('登録日時', default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'
