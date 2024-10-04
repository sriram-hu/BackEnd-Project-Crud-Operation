from django.urls import path
from .views import index,mainpage,Login,AdminLogin,Studentform

urlpatterns = [
    path('',index,name='index'),
    path('mainpage/',mainpage,name='mainpage'),
    path('Login/',Login, name='Login'),
    path('AdminLogin/',AdminLogin, name='AdminLogin'),
    path('Studentform/',Studentform, name='Studentform'),

]