from django.urls import path,include
from rest_framework import routers
from api.views import BookingViewset, SignUpViewset, loginVisewset, ConfirmationViewset

router = routers.DefaultRouter()
router.register(r'booking',BookingViewset,basename='booking')
router.register(r'SignUp',SignUpViewset,basename='SignUp')
router.register(r'login',loginVisewset,basename='login')
router.register(r'Confirmation',ConfirmationViewset,basename='Confirmation')

urlpatterns = [
    path('',include(router.urls))
]