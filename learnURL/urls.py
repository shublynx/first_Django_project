from django.conf.urls import url
from learnURL import views

# template tagging
app_name = 'learnURL'
urlpatterns = [
    url('home/',views.index,name='index'),
    url('relative/', views.relative,name='relative'),
    url('other/',views.other,name='other')
]