# Gallery-App
 

## Author
Kojwang Elibora Ochieng

### Description
This is a photo gallery web application that showcases beautiful pictures. Users get can view photos uploaded by admin. Users can also see photos based on the title and category they like. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories and titles.

### features
- The home page allows users to browse images 
- Users can search for images based categories
- Admin can upload images from a django dashboard
- Users can also upload their images

### Deployed link


##### Cloning the repository:

 


#### Install and activate Virtual
 ```bash 
-  - pipenv shell 
```  

##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
#### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations <database name>
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 

### run app
 ```bash 
 python manage.py runserver 
```  
##### Runing the application 
 ```bash 
 python manage.py runserver
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.1](https://docs.djangoproject.com/en/3.0/) 
* [Heroku](https://heroku.com)  
* [Git](for version control)

## License

- Licensed under[MIT license](license).