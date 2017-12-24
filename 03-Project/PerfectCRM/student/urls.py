
from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.index, name="stu_index"),
    # url(r'^customers$', views.customer_list, name="customer_list"),
    # url(r'^customers$', views.index, name="index"),
]
