from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('login', views.login),
    #url("user/detail", views.get_user),
    url("article/detail", views.get_article),
    url('article/create', views.create_article),
    url('article/update', views.update_article),
]
