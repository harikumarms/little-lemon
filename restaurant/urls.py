from django.urls import path, include
from rest_framework import routers
from .views import MenuApi, BookingApi, SingleMenuApi
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', BookingApi, basename='booktable')

urlpatterns = [
        path('menu', MenuApi.as_view()),
        path('menu/<int:pk>', SingleMenuApi.as_view()),
        path('booking/', include(router.urls)),
        path('api-token-auth', obtain_auth_token)
    ]