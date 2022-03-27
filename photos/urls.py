from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.welcome,name='welcome'),
    re_path(r'^today/$',views.photos_of_day,name='photoToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhoto'),
    re_path('search/', views.search, name='search') 
]