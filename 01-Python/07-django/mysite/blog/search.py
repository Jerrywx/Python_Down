# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

# 表单
def search_form(request):
    return render_to_response('search_form.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'

    #GET 方法
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

#
# def search_post(request):
#     # return render_to_response('search_form.html')
#     return render_to_response('search_post.html')

# 接收请求数据
def post_search(request):
    request.encoding = 'utf-8'

    # POST 方法
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "search-post.html", ctx)
