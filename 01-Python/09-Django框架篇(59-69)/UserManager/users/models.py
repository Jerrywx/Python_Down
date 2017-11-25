from django.db import models

# Create your models here.

# 班级
class Classes(models.Model):
    caption = models.CharField(max_length=32)


# 学生
class Student(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ForeignKey('Classes')


# 老师
class Teacher(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ManyToManyField('Classes')

# 管理账户
class Administrator(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)