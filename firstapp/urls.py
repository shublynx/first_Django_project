from django.conf.urls import url
from firstapp import views

urlpatterns = [

    url('home/', views.home , name='home'),
    url('users/', views.users , name='home'),
    url('index',views.index, name='index'),
    url('help/', views.help , name='help'),
    url('formpage/',views.form_name_view),
    url('signup/',views.formdataSave)
]
