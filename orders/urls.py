from django.urls import path
from .views import OrderListCreateView, OrderDetailView, OrderItemCreateView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:order_id>/items/', OrderItemCreateView.as_view(), name='order-item-create'),
]