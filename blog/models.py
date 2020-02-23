from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(verbose_name='タイトル', max_length=200)
  text = models.TextField(verbose_name='本文')
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def approved_comments(self):
    return self.comments.filter(approved_comment=True)

  def __str__(self):
    return self.title


class Comment(models.Model):
  post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
  author = models.CharField(verbose_name='投稿者', max_length=200, default='名無し')
  text = models.TextField()
  created_date = models.DateTimeField(verbose_name='投稿日', default=timezone.now)
  approved_comment = models.BooleanField(default=False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def __str__(self):
    return self.text