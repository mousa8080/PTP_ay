# """
# URL configuration for PTPay project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path,include
# from accounts.views import MyObtainTokenPairView
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path ('api/',include('accounts.urls')),
#         path('api/', include('core.urls')),  # Include URLs from core app
#     path ('api/token/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
#     path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
#     path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/',include('accounts.urls')),
    # path ('api/',include('core.urls')),
    path('payments/', include('payments.urls')),
    path('transportation/', include('transportation.urls')),

]