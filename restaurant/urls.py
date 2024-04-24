from django.urls import path, include
from rest_framework import routers
from .views import MenuView, SingleMenuView, BookingViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', BookingViewSet, basename='booktable')

urlpatterns = [
        path('menu', MenuView.as_view()),
        path('menu/<int:pk>', SingleMenuView.as_view()),
        path('booking/', include(router.urls))
    ]