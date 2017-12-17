from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

from django.http import HttpResponse
from django.shortcuts import render,redirect
from userInfo import models


# userList = []

def userInfo(req):
    print("===============================")

    if req.method == "POST":
        username = req.POST.get("username", None)
        sex = req.POST.get("sex", None)
        emial = req.POST.get("emial", None)

        user = {"username": username, "sex":sex, "emial":emial}

        models.User.objects.create(
            username=username,
            sex = sex,
            emial = emial,
        )

        userList = models.User.objects.all()
        return render(req, 'userInfo.html', {"userList" : userList})
    return render(req, 'userInfo.html')



def year_archive(req, year, month):
    return HttpResponse("year_archive" + year + "year" + month + "month")


def alias_name(req, name):
    return HttpResponse(name)


# 用户登录
def login(req):

    if req.method == "POST":
        print("This is POST")

    return render(req, "login.html")


# 获取用户信息
def getUserInfo(req):

    name = "wang"
    age = "25"
    emial = "23600000@qq.com"

    # return render(req, "getUserInfo.html", {"name":name,"age":age, "emial":emial})
    # return render(req, "getUserInfo.html", locals())
    return redirect("http://www.baidu.com")



def test(req):
    return HttpResponse("This is a Test")






