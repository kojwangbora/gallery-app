from django.db import models
from pickle import FALSE, TRUE
from cloudinary.models import CloudinaryField


# Create your models here.
class Location(models.Model):
    location_name =models.CharField(max_length=50, blank=TRUE, default=None)
    location_town = models.CharField(max_length=25)

    def save_location(self):
        self.save()
    
    def __str__(self):
        return self.location_name
    
    class Meta:
        ordering = ['location_name']

class Category(models.Model):
    category = models.CharField(max_length =30, null=TRUE, default=None)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.category


class Image(models.Model):
    photo_name = models.CharField(max_length=30)
    Description = models.TextField()
    image = models.ImageField(upload_to = 'photo-gallery', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=TRUE)
    category = models.ManyToManyField(Category)
    upload_date = models.DateTimeField(auto_now_add=True,null=True)
    
   
    def save_photo(self):
        self.save()

    @classmethod
    def search_by_category(cls, category):
        photos = cls.objects.filter(category__category__icontains = category)
        return photos

      
    @classmethod
    def filter_by_location(cls, location):
        photos = cls.objects.filter(location__location__icontains = location)
        return photos
        
    def __str__(self):
        return self.photo_name
    
    
        
    
     
