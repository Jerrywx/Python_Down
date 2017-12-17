from django.db import models

# Create your models here.

# 测试模型

class User(models.Model):

    username = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    emial = models.CharField(max_length=20)

    def __str__(self):
        return self.username + self.sex
