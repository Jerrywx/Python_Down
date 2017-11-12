from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from Models.models import Test
from Models.models import Author
from Models.models import Books
from Models.models import MyBook
from Models.models import Xbook
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
    # author = Author()
    # author.name = "wxiao"
    # author.telNum = "17718576672"
    # author.address = "Beijing"
    # author.save()
    #
    # Books.objects.create(
    #     namew = "iOS 开发",
    #     price = 78,
    #     type = "iOS",
    #     authorer = author,
    # )

    # 多表联合 多对多 插入一条数据
    # author = Author()
    # author.name = "余秋雨"
    # author.telNum = "1111111"
    # author.address = "未知"
    # author.save()
    #
    # author2 = Author()
    # author2.name = "余秋雨2"
    # author2.telNum = "1111111"
    # author2.address = "未知"
    # author2.save()
    #
    # book = Xbook()
    # book.name = "君子之道"
    # book.price = 119
    # book.type = "文学类"
    # book.save()
    #
    # book.author.add(author)

    # 多表联合 多对多 插入多条数据
    # 读取作者1
    author1 = Author.objects.filter(id="2")[0]
    author2 = Author.objects.filter(id="5")[0]
    book = Xbook.objects.filter(id="1")[0]
    print("=========", author1.name, author2.name, book.type)
    book.author.add(author1, author2)



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