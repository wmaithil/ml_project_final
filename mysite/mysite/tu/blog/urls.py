from django.urls import path
from . import views 

urlpatterns = [
    # blog_pages urls

    path('mauri',views.mauritius,name='mauri'),
    path('beach',views.beach,name='beach'),
    path('sunset',views.sunset,name='sunset'),
    path('home',views.home,name='home'),
    

    #authentication urls

    path('signup',views.signup,name='signup'),
    path('djlogin',views.handleLogin,name='handleLogin'),
    path('logout',views.handleLogout,name='handleLogout'),
    path('', views.blog, name='blog'),
]
