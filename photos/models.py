from django.db import models
from pickle import FALSE, TRUE
import datetime as dt


# Create your models here.
class Location(models.Model):
    location_name =models.CharField(max_length=50, blank=TRUE, default=None)
    location_town = models.CharField(max_length=25)

    def save_location(self):
        self.save()
    
    def __str__(self):
        return self.location_name
    
    # class Meta:
    #     ordering = ['location_name']

class Category(models.Model):
    category = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.category


class Image(models.Model):
    photo_name = models.CharField(max_length=30)
    Description = models.TextField()
    image = models.ImageField(upload_to = 'photo-gallery', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=TRUE)
    category = models.ManyToManyField(Category, on_delete=models.CASCADE, null=TRUE)
    upload_date = models.DateTimeField(auto_now_add=True,null=True)
    
   
    def save_photo(self):
        self.save()
        
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(upload_date__date = today)
        return photos
    
    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(upload_date__date = date)
        return photos
    
    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images
