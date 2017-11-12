from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from Models.models import Test
from Models.models import Author
from Models.models import Books
from Models.models import MyBook
from Models import models



def test(req):

    # 加入数据 1
    # test1 = Test()
    # test1.name = "wxiao"
    # test1.size = "1000000"
    # test1.time = "现在"
    # test1.save()

    # 加入数据 2
    models.Test.objects.create(name="张三", size="431", time="哈哈")

    return HttpResponse("This is a Test！！！1")

def addbook(req):

    # 添加一对多 数据
    # 通过键值对创建
    # MyBook.objects.create(
    #     name = "Python",
    #     type = "IT",
    #     price= 66,
    #     # author_id = 2,
    # )

    # 一对多 表 插入数据        方法一:
    # Books.objects.create(
    #     namew="iOS 开发",
    #     price=78,
    #     type="iOS",
    #     authorer_id = "2",
    # )

    # 一对多 表 插入数据        方法一:
    author = Author()
    author.name = "wxiao"
    author.telNum = "17718576672"
    author.address = "Beijing"
    author.save()

    Books.objects.create(
        namew = "iOS 开发",
        price = 78,
        type = "iOS",
        authorer = author,
    )




    #
    # book = Book()
    # book.name = "Python"
    # book.type = "IT"
    # book.price = 100
    # # book.author = author
    # # book.author.add(*author)
    #
    # book.save()

    return HttpResponse("add Book!!!!")


# 获取书籍
def getbook(req):

    # 更新内容
    # MyBook.objects.filter(id="2").update(name="wxiao")

    # 读取数据
    # book = MyBook.objects.get(id="2")

    # 读取数据
    # book = MyBook.objects.filter(id="2")[0]

    # str = "book:" + book.name + "<br>Type:" + book.type



    # 读取数据熟属性
    # name = MyBook.objects.filter(id="2").values("name")[0]
    # str = "book:" + name['name'] +"!!!"
    # return  HttpResponse(str)

    # 批量获取
    list = MyBook.objects.filter(name="Python")

    for obj in list[2:4]:
        print("------", obj.name , obj.id)

    return HttpResponse("成功!!")