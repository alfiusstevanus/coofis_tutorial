from django.urls import include, path
from apps.attachments.views import attachment_views
from django.conf import settings
from django.views.static import serve

app_name = "attachments"
urlpatterns = [
    path("", attachment_views.AttachmentListCreateAPIView.as_view(), name="attachment-list"),
    path("create/", attachment_views.AttachmentListCreateAPIView.as_view(), name="attachment-create"),
    path("<str:id>/", attachment_views.AttachmentRetrieveUpdateDestroyAPIView.as_view(), name="attachment-detail"),
    path("<str:id>/", attachment_views.AttachmentRetrieveUpdateDestroyAPIView.as_view(), name="attachment-update"),
    path("<str:id>/", attachment_views.AttachmentRetrieveUpdateDestroyAPIView.as_view(), name="attachment-delete"),
    path("mediafiles/<path:path>", serve, {'document_root': "mediafiles/attachments/"}),
]