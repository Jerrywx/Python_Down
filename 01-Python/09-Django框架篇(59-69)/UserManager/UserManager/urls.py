"""UserManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from users import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 登录
    # url(r'^login', views.login),
    url(r'^login', views.Login.as_view()),

    # 注销
    url(r'^logout', views.login),
    url(r'^index', views.index),
    # 班级
    url(r'^classes', views.classes),
    # 学生
    url(r'^student', views.student),
    # 老师
    url(r'^teacher', views.teacher),

    url(r'^js_cookie', views.js_cookie),
    url(r'^session', views.session),

]
