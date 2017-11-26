from django.shortcuts import render, redirect

# Create your views here.
from users import models
from django.http import HttpResponse

from django import views
from django.utils.decorators import method_decorator


# 装饰器
def outer(func):
    def inner(request, *args, **kwargs):
        print(request.method, "====================")
        return func(request, *args, **kwargs)
    return inner

# 一、使用 CBV
class Login(views.View):

    def dispatch(self, request, *args, **kwargs):
        rep = super(Login, self).dispatch(request, *args, **kwargs)
        return rep

    # @method_decorator(outer)
    def get(self, request, *args, **kwargs):

        return render(request, 'login.html', {"msg":""})

    # @method_decorator(outer)
    def post(self, request, *args, **kwargs):
        user = request.POST.get("username")
        pwd = request.POST.get("password")

        u = mm = models.Administrator.objects.filter(username=user, password=pwd)

        if u:
            # 设置 session
            request.session['is_login'] = True
            request.session['username'] = user
            rep = redirect('/index.html')
            # 设置 cookie
            # rep.set_cookie('username', user, max_age=60 * 3)
            return rep
        else:
            massage = "用户名或密码错误!"
            return render(request, 'login.html', {"msg": massage})

# 注销
def logout(request):
    rep = redirect('/login.html')
    rep.set_cookie('username', "")
    return rep

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
    # 读取cookie
    # name = request.COOKIES.get("username")
    # 读取 session
    name = request.session.get('username')
    request.session
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

# session
def session(request):
    request.session['value'] = "kkkk"
    print("------------- session")
    return HttpResponse("OK")
