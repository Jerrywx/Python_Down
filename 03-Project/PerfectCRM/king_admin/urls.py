
from django.conf.urls import url
from king_admin import views

urlpatterns = [
    url(r'^$', views.index, name="table_index"),
]
