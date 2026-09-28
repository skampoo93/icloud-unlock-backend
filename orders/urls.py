from django.urls import path
from .views import OrderCreateView, MyOrdersView, AdminOrderListView, AdminOrderDetailView

urlpatterns = [
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("mine/", MyOrdersView.as_view(), name="order-mine"),
    path("admin/", AdminOrderListView.as_view(), name="order-admin-list"),
    path("admin/<int:pk>/", AdminOrderDetailView.as_view(), name="order-admin-detail"),
]
