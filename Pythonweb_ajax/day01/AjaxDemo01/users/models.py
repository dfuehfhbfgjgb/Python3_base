from django.db import models


# Create your models here.
class User(models.Model):
    uname = models.CharField('用户名', max_length=30, unique=True)
    upwd = models.CharField('密码', max_length=30)
    nickname = models.CharField('昵称', max_length=30)

    class Meta():
        db_table = 'user'
