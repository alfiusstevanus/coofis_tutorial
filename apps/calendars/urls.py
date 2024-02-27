from django.urls import include, path
from apps.calendars.views import *
from django.http import HttpResponse

app_name = "calendars"
urlpatterns = [
    path("", lambda request: HttpResponse("Hello, Calendar!")),
]