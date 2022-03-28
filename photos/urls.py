from django.urls import re_path,path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^$',views.welcome,name='welcome'),
    re_path('search/', views.search, name='search'),
    path(r'^photodetails/',views.photos_of_day, name = 'photodetails'),
    path(r'photo_details/<int:pk>',views.photo_details, name ='photo_details')
     
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)