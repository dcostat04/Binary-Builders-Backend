from django.urls import path,include
from rest_framework import routers
from api.views import BookingViewset

router = routers.DefaultRouter()
router.register(r'booking',BookingViewset,basename='booking')

urlpatterns = [
    path('',include(router.urls))
]