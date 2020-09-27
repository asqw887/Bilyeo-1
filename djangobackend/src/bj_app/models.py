from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class BJ_ITEM(models.Model):
    bj_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bj_title = models.CharField(max_length=50)
    bj_content = models.TextField()
    bj_reportingTime = models.DateField()
    bj_views = models.IntegerField()

class BJ_BOARD(models.Model):
    bj_item = models.ForeignKey(BJ_ITEM, on_delete=models.CASCADE)

class BJ_COMMENT(models.Model):
    bj_comment_id = models.ForeignKey(BJ_ITEM, on_delete=models.CASCADE)
    bj_comment_datetime = models.DateTimeField()
    bj_comment_content = models.TextField()