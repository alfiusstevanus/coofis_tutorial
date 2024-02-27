from django.urls import include, path
from apps.posts.views import post_views

app_name = "posts"
urlpatterns = [
        path("", post_views.PostListCreateAPIView.as_view(), name="post-list"),
        path("create/", post_views.PostListCreateAPIView.as_view(), name="post-create"),
        path("<str:id>/", post_views.PostRetrieveUpdateDestroyAPIView.as_view(), name="post-detail"),
        path("<str:id>/", post_views.PostRetrieveUpdateDestroyAPIView.as_view(), name="post-update"),
        path("<str:id>/", post_views.PostRetrieveUpdateDestroyAPIView.as_view(), name="post-delete"),
]