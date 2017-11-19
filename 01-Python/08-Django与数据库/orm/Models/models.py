from django.db import models

# Create your models here.

from django.db import models

# 测试模型
class Test(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    def __str__(self):
        return self.name


# 书籍模型
class Book(models.Model):
    name = models. CharField(max_length=20)
    price = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    author = models.ManyToManyField("Author")

    # def __str__(self):
    #     return self.name

class MyBook(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    type = models.CharField(max_length=10)

# 作者
class Author(models.Model):
    name = models.CharField(max_length=20)
    telNum = models.CharField(max_length=15)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Books(models.Model):
    namew = models.CharField(max_length=20)
    price = models.IntegerField()
    type = models.CharField(max_length=10)
    authorer = models.ForeignKey("Author")


class Xbook(models.Model):
    namew = models.CharField(max_length=20)
    price = models.IntegerField()
    type = models.CharField(max_length=10)
    author = models.ManyToManyField("Author")


# 创建联合唯一表
class Book2Author(models.Model):
    book = models.ForeignKey("Author")
    author = models.ForeignKey("MyBook")

    class Meta:
        unique_together = ["author", "book"]


class Movies(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    address = models.CharField(max_length=10)
    length = models.FloatField()
    director = models.CharField(max_length=30)










