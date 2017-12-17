

from django.conf.urls import url
from django.contrib import admin
from userInfo import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    #
    # url(r'^login', views.login),
    # url(r'^test/', views.test, name='test'),


    url(r'test/', views.test),
    url(r'getUserInfo/', views.getUserInfo),
]