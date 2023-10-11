from django.urls import path,include
from rest_framework import routers
from api.views import BookingViewset, SignUpViewset, loginVisewset

router = routers.DefaultRouter()
router.register(r'booking',BookingViewset,basename='booking')
router.register(r'SignUp',SignUpViewset,basename='SignUp')
router.register(r'login',loginVisewset,basename='login')

urlpatterns = [
    path('',include(router.urls))
]