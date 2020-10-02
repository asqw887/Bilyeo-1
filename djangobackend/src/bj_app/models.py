from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class BJ_ITEM(models.Model):
    bj_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    bj_title = models.CharField(max_length=100)
    bj_content = models.TextField(max_length=200)
    published = models.DateTimeField(auto_now_add=True) 
    bj_views = models.IntegerField(blank=True, null=True,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True,default='')

    def __str__(self):
        return self.bj_title
    
    class Meta:
        ordering = ('-published', '-pk')

class BJ_BOARD(models.Model):
    objects = models.Manager()
    bj_item = models.ForeignKey(BJ_ITEM, on_delete=models.CASCADE)

class BJ_COMMENT(models.Model):
    objects = models.Manager()
    bj_comment_id = models.ForeignKey(BJ_ITEM, on_delete=models.CASCADE)
    bj_comment_datetime = models.DateTimeField()
    bj_comment_content = models.TextField()