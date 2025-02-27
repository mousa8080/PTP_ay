

from accounts.views import RegisterView
from rest_framework import routers


routers = routers.DefaultRouter()

routers.register('RegisterView',RegisterView)


urlpatterns = [
    
] + routers.urls
