from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from . models import Image

# Create your views here.
def welcome(request):
    photos = Image.objects.all()
    return render(request,'welcome.html', {"photos": photos})

def photos_of_day(request):
    
    photos = Image.objects.all()
    context= {"photos": photos}
    
    return render(request, 'all-photos/today-photos.html', context)

def photo_details(request, pk):
    photos = Image.objects.get(pk=pk)

    context = {
         "photos":photos
     }
    return render(request, 'all-photos/photo_details.html', context)


def filter_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.filter_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/filter.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/filter.html',{"message":message})  

# def convert_dates(dates):
#     #Function that gets the weekday number for the day.
#     day_number = dt.date.weekday(dates)
#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def past_days_photos(request,past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False
    
#     if date == dt.date.today():
#         return redirect(photos_of_day)
    
#     photos = Image.days_photos(date)

#     return render(request, 'all-photos/past-photos.html', {"date": date,"photos":photos})


def search(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-photos/search.html',{"message":message})


    #  def details(request, pk):
    # eachimage = Images.objects.get(id=pk)
    # context = {
    #     'eachimage':eachimage
    # }

    # context = {
    #     'eachimage':eachimage
    # }