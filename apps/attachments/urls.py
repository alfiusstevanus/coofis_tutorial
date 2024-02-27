from django.urls import include, path
from apps.attachments.views import *
from django.http import HttpResponse

app_name = "attachments"
urlpatterns = [
    path("", lambda request: HttpResponse("Hello, attachment!")),
]