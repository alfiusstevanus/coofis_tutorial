from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework import permissions
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Coofis API Documentation",
        default_version='v1',
        description="Documentation for Coofis API",
        contact=openapi.Contact(email="coofis@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('account/', include('apps.accounts.urls')),
        path('post/', include('apps.posts.urls')),
        path('calendar/', include('apps.calendars.urls')),
        path('event/', include('apps.events.urls')),
        path('attachment/', include('apps.attachments.urls')),
    ])),
    path("mediafiles/attachments/<path:path>", serve, {'document_root': "mediafiles/attachments/"}),
] 