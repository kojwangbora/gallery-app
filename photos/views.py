from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from . models import Image

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def photos_of_day(request):
    date = dt.date.today()

    photos = Image.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"date": date,"photos":photos})

    

def convert_dates(dates):
    #Function that gets the weekday number for the day.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_photos(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(photos_of_day)
    
    photos = Image.days_photos(date)

    return render(request, 'all-photos/past-photos.html', {"date": date,"photos":photos})

     