from django.urls import path,include
from rest_framework import routers
from api.views import BookingViewset, SignUpViewset

router = routers.DefaultRouter()
router.register(r'booking',BookingViewset,basename='booking')
router.register(r'SignUp',SignUpViewset,basename='SignUp')

urlpatterns = [
    path('',include(router.urls))
]