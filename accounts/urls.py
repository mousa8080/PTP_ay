from accounts.views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    path ('jwt/create/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/user/', RegisterUserView.as_view(), name='register-user'),
    path('register/driver/', RegisterDriverView.as_view(), name='register-driver'),
    
    ]
