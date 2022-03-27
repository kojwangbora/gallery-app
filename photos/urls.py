from django.urls import re_path,path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^$',views.welcome,name='welcome'),
    re_path(r'^today/$',views.photos_of_day,name='photoToday'),
    path(r'^photodetails/<int:',views.photos_of_day,name = 'photodetails'),
    re_path('search/', views.search, name='search') 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)