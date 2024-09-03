from django.urls import path
from . import views

# A list of all urls that can be accessed to this particular hellop app
# When "" is visited, the views.index function will be called.
# Give a name to a path can be useful
urlpatterns = [
    path("", views.index, name="index"),
    path("honggang", views.honggang, name="honggang"),
    path("<str:name>", views.greet, name="greet") 
]