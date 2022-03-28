from django.urls import re_path,path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^$',views.welcome,name='welcome'),
    re_path('search/', views.search, name='search'),
    re_path('filter',views.filter_results,name='filter_results'),
    # path(r'^photodetails/<int:photo_id>',views.photos_of_day,name = 'photodetails'),
     
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)