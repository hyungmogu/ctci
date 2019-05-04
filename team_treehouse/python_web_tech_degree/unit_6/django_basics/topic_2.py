# ============= Part 1 =============
# Challenge Task 1 of 2
# Import HttpResponse from the django.http module.

#<PROJECT>/views.py
from django.http import HttpResponse

# Challenge Task 2 of 2
# Great! Now create a view named index that returns an HttpResponse with the string "Hello Treehouse".

#<PROJECT>/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Treehouse")


# ============= Part 2 =============
# Challenge Task 1 of 2
# We need to add a URL for the view we created in the last challenge. First, though, import the views module from the current directory. Remember, the current directory is referenced as a single dot or period.

#newspaper/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
]

# Challenge Task 2 of 2
# Now we need to make a url for our index view. Add a url to urlpatterns with a pattern for an empty string that points to the index view from views.

#newspaper/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index)
]