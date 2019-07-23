from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [

    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^$', views.HomePage.as_view(), name='Home'),
    url(r'^registration/$', views.Registration.as_view(), name='registration'),
    path('<str:user>/home/', views.UserHome.as_view(), name='UserHome'),
    path('<str:user>/profile/', views.UserProfile.as_view(), name='UserProfile'),
    path('/login/', views.Login.as_view(), name='Login'),

]
