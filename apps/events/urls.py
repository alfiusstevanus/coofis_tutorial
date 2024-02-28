from django.urls import include, path
from apps.events.views import event_views
from django.conf import settings

app_name = "events"

urlpatterns = [
    path("", event_views.EventListCreateAPIView.as_view(), name="event-list"),
    path("create/", event_views.EventListCreateAPIView.as_view(), name="event-create"),
    path("<str:id>/", event_views.EventRetrieveUpdateDestroyAPIView.as_view(), name="event-detail"),
    path("<str:id>/", event_views.EventRetrieveUpdateDestroyAPIView.as_view(), name="event-update"),
    path("<str:id>/", event_views.EventRetrieveUpdateDestroyAPIView.as_view(), name="event-delete"),
]