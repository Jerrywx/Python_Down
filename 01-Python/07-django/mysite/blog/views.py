from django.shortcuts import render, redirect

# Create your views here.


from django.http import HttpResponse

def hello(request):
    print("======",request)
    context = {}
    context['hello'] = "Hello My World!"
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello World!")


def helloPython(request):
    return HttpResponse("Hello Python!")

def test(reuqest):
    return HttpResponse("This is a Test")


def index(req):

    if req.method == "POST":
        username = req.POST.get("username")
        pwd = req.POST.get("pwd")
        if username == "wxiao" and pwd == "123456":
            return HttpResponse("登录成功")

    return render(req, 'login.html')


def login(req):

    name = 'wxiao!!!'
    test = 'TTTT'

    # return render(req, 'login.html', {'name':"wxiao", 'test':"TTTT"})
    return render(req, 'login.html', locals())


# 用户登录操作
def loginAction(req):

    if req.method == "POST":
        username = req.POST.get("username")
        pwd = req.POST.get("pwd")
        if username == "wxiao" and pwd == "123":
            return redirect('base.html')

    #     print("用户名:", request.POST.get("username"))
    #     print("用户名:", request.POST.get("pwd"))

    return render(req, 'user_login_views.html')



