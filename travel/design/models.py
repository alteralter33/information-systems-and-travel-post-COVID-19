from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Username')
    comment_content = models.TextField(verbose_name='Comment content')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='Comment time')

class Meta:
    db_table = "comments"
    ordering = ['-comment_time']