# from django.urls import path
# from . import views

# urlpatterns = [
#     # Endpoint القديم للنصوص (legacy)
#     path('do_get/', views.do_get, name='do_get'),
    
#     # Endpoint الجديد باستخدام DRF (بيقدم رد بصيغة JSON)
#     path('payment/', views.PaymentAPIView.as_view(), name='payment-api'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
