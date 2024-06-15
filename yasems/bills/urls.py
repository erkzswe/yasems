from django.urls import path
from bills import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductView.as_view()),
    path('bills/', views.BillListView.as_view()),
    path('bills/<int:pk>/', views.BillView.as_view()),
]