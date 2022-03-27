from django.test import TestCase
from .models import Location, Category, Image
import datetime as dt


# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.westlands= Location(location_name = 'westlands', location_town ='Nairobi')
        self.westlands.save_location()
    
        
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.westlands,Location))
    
       