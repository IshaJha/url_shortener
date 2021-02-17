from django.urls import path
from .views import generateURL,getURL

urlpatterns = [
    path('generateURL/', generateURL, name='generateURL'),
    path('getURL/<slug:slug>', getURL, name='getURL'),
    # path('getURL/<int:key>', getURL, name='getURL'),
]

#  C:\Users\Isha\.virtualenvs\url_shortener-cCjrrS1C  #virtual environment place
 
#  https://bit.ly/3c4vl10  # URL format

# https://www.freecodecamp.org/news/building-a-simple-url-shortener-with-just-html-and-javascript-6ea1ecda308c/

# https://www.geeksforgeeks.org/7-cool-python-project-ideas-for-intermediate-developers/

# https://realpython.com/intermediate-python-project-ideas/