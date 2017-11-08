from django.shortcuts import render

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

