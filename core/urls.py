from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentViewSet, DepositViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)  # CRUD for users
router.register(r'payments', PaymentViewSet, basename='payment')  # Payment operations
router.register(r'deposits', DepositViewSet, basename='deposit')  # Deposit operations

urlpatterns = [
    path('', include(router.urls)),
]
