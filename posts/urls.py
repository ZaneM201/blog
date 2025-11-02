from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, DraftPostListView, ArchivedPostListView


urlpatterns = [
    path("", PostListView.as_view(), name="posts_list"),
    path("detailed/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path("drafts/", DraftPostListView.as_view(), name="post_draft"),
    path("archived/", ArchivedPostListView.as_view(), name="archived_list"),
]