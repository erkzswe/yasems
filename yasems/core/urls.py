from core import views

from django.urls import include, path
from bills.urls import urlpatterns as bills_urls


urlpatterns = [
    path("", views.root),
    path("users/", views.UserList.as_view(), name="users-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="users-detail"),
] + bills_urls
