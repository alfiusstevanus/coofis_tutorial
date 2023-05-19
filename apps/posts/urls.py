from django.urls import include, path
from apps.posts.views import post_views

app_name = "posts"
urlpatterns = [
        path("", post_views.PostListCreateAPIView.as_view(), name="post-list"),
        path("create/", post_views.PostListCreateAPIView.as_view(), name="post-create"),
        path("detail/<str:id>/", post_views.PostRetrieveUpdateAPIView.as_view(), name="post-detail"),
        path("update/<str:id>/", post_views.PostRetrieveUpdateAPIView.as_view(), name="post-update"),
        path("delete/<str:id>/", post_views.PostDestroyAPIView.as_view(), name="post-delete"),


                # path("refresh/", auth_views.RefreshGenericAPIView.as_view(), name="auth-refresh"),
                # path("logout/", auth_views.LogoutGenericAPIView.as_view(), name="auth-logout"),
]