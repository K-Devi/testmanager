from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('sections/', views.add_section, name='sections'),
    path('catalogs/', views.catalog, name='catalog'),
    path('newtest/', views.newtest, name='newtest'),
    path('testlist/', views.testlist, name='testlist'),
    path('topics/', views.add_topic, name='topics'),
    path('topics/questions', views.add_question, name='questions'),
]
