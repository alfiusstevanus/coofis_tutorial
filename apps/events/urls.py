from django.urls import include, path
from apps.events.views import *
from django.http import HttpResponse

app_name = "events"

urlpatterns = [
    path("", lambda request: HttpResponse("Hello, Event!")),
]

# urlpatterns = [
#     path(
#         "",
#         include(
#             [
#             ]
#         ),
#     ),
# ]