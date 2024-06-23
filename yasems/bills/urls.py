from django.urls import path
from bills import views

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="products-list"),
    path("products/<int:pk>/", views.ProductView.as_view(), name="products-detail"),
    path("bills/", views.BillListView.as_view(), name="bills-list"),
    path("bills/<int:pk>/", views.BillView.as_view(), name="bills-detail"),
    path("payments/", views.PaymentListView.as_view(), name="payments-list"),
    path("payments/<int:pk>/", views.PaymentView.as_view(), name="payments-detail"),
]
