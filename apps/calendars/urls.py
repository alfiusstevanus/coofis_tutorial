from django.urls import include, path
from apps.calendars.views import calendar_views
from django.conf import settings

app_name = "calendars"
urlpatterns = [
    path("", calendar_views.CalendarListCreateAPIView.as_view(), name="calendar-list"),
    path("create/", calendar_views.CalendarListCreateAPIView.as_view(), name="calendar-create"),
    path("<str:id>/", calendar_views.CalendarRetrieveUpdateDestroyAPIView.as_view(), name="calendar-detail"),
    path("<str:id>/", calendar_views.CalendarRetrieveUpdateDestroyAPIView.as_view(), name="calendar-update"),
    path("<str:id>/", calendar_views.CalendarRetrieveUpdateDestroyAPIView.as_view(), name="calendar-delete"),
]