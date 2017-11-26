from django.shortcuts import render, redirect

# Create your views here.
from users import models
from django.http import HttpResponse


# 登录函数
def login(request):

    massage = ""
    if request.method == "POST":

        user = request.POST.get("username")
        pwd = request.POST.get("password")

        u = mm = models.Administrator.objects.filter(username=user, password=pwd)

        if u:
            rep = redirect('/index.html')
            rep.set_cookie('username', user, max_age=60 * 3)
            # rep.set_cookie('password', pwd)
            return rep
            # return render(request, 'index.html', {'username': user})
        else:
            massage = "用户名或密码错误!"

    return render(request, 'login.html', {"msg":massage})


#
def index(request):
    name = request.COOKIES.get("username")
    if name:
        return render(request, 'index.html', {'username': name})
    else:
        return redirect('/login.html')

# jquery
def js_cookie(req):
    print("--------------------")
    print(req.COOKIES)
    print("--------------------")
    # return HttpResponse("OK")
    return render(req, 'js_cookie.html')