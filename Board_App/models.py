from django.db import models
from django.utils import timezone


"""スレッド"""
class Post(models.Model):
    """必須"""
    title = models.CharField('スレッド名', max_length=50)
    """必須 / デフォルトに現在日時を指定"""
    created_at = models.DateTimeField('登録日時', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        """管理画面での表示内容の変更"""
        verbose_name = 'スレッド'
        verbose_name_plural = 'スレッド'
        """データベースの名前変更"""
        db_table = 'スレッド'

"""コメント"""
class Comment(models.Model):
    """スレッドにコメントを紐付け。　スレッドが削除されればコメントも削除"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    """必須"""
    author = models.CharField('ニックネーム', max_length=50)
    """必須"""
    text = models.TextField('コメント内容')
    """必須 / デフォルトに現在日時を指定"""
    created_at = models.DateTimeField('登録日時', default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        """管理画面での表示内容の変更"""
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'
        """データベースの名前変更"""
        db_table = 'コメント'
