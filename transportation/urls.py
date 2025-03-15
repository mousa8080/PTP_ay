from .views import *
from rest_framework import routers
from django.urls import path,include
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'vehicle_trackings', VehicleTrackingViewSet)
router.register(r'driver_earnings', DriverEarningsViewSet)
router.register(r'reports', ReportViewSet)
urlpatterns = [
  path('', include(router.urls)),
]

