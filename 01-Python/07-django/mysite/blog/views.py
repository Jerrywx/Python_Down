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


