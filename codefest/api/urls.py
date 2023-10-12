from django.urls import path,include
from rest_framework import routers
from api.views import BookingViewset, SignUpViewset, loginVisewset, ConfirmationViewset, Consultation_detailsViewset,userdetailedViewset, MeetingLinkViewset

router = routers.DefaultRouter()
router.register(r'booking',BookingViewset,basename='booking')
router.register(r'SignUp',SignUpViewset,basename='SignUp')
router.register(r'login',loginVisewset,basename='login')
router.register(r'Confirmation',ConfirmationViewset,basename='Confirmation')
router.register(r'Consultation_details',Consultation_detailsViewset,basename='Consultation_details')
router.register(r'userdetailed',userdetailedViewset,basename='userdetailed')
router.register(r'MeetingLink',MeetingLinkViewset,basename='MeetingLink')


urlpatterns = [
    path('',include(router.urls))
]