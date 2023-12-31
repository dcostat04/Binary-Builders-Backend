from django.shortcuts import render
from rest_framework import viewsets
# from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response
from api.models import Booking, SignUp, Confirmation, Consultation_details
from rest_framework import status
import json
from django.http import HttpResponse
from django.core.mail import send_mail



class BookingViewset(viewsets.ModelViewSet):
    def create(self,request):
        try:
            if len(request.body) > 0:
                output_dict = json.loads(request.body.decode("utf-8"))
                data = dict()
                data['name'] = output_dict.get('name')
                data['email'] = output_dict.get('email')
                data['phone'] = output_dict.get('phone')
                data['address'] = output_dict.get('address')
                data['issue'] = output_dict.get('issue')
                data['description'] = output_dict.get('description')
                data['citizenship_id'] = output_dict.get('citizenship_id')
                data['relation'] = output_dict.get('relation')
    

                # print(data)

                booking_create = Booking(**data)
                booking_create.save()

                subject = 'Detailed explanation of concerned issue'
                # message = 'Hi'
                message = "Thank you for reaching out to us. We are happy to help and listen to you. Please visit the link and provide a detailed overview of you concern. USERNAME:" + data['email'] + "PASSWORD:" + "random@123"
                from_email = 'krangarius@gmail.com'
                recipient_list = [data['email']]

                send_mail(subject, message, from_email, recipient_list)
                return HttpResponse("Emails sent successfully")
            return Response(
                    {"status":"OKAY","data":data}, status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"status":"ERROR","ERROR":str(e)}
            )

class SignUpViewset(viewsets.ModelViewSet):
    def create(self,request):
        try:
            if len(request.body) > 0:
                output_dict = json.loads(request.body.decode("utf-8"))
                data = dict()
                data['firstname'] = output_dict.get('firstname')
                data['lastname'] = output_dict.get('lastname')
                data['phone_number'] = output_dict.get('phone_number')
                data['email'] = output_dict.get('email')
                data['address'] = output_dict.get('address')
                data['city'] = output_dict.get('city')
                data['password'] = output_dict.get('password')
                data['confirm_password'] = output_dict.get('confirm_password')

                # print(data)

                SignUp_create = SignUp(**data)
                SignUp_create.save()

                return Response(
                    {"status":"OKAY","data":data}, status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"status":"ERROR","ERROR":str(e)}
            )

class loginVisewset(viewsets.ModelViewSet):
    def list(self,request):
        try:
            if len(request.body) > 0:
                output_dict = json.loads(request.body.decode("utf-8"))
                username = output_dict.get('email')
                password = output_dict.get('password')
                # print(data)
                myobj = SignUp.objects.filter(email=username,password=password)
                # print(myobj)
                if len(myobj)>0:
                    return Response(
                        {"User":True}
                    )
                else:
                    return Response(
                        {"User":False}
                    )
        except Exception as e:
            return Response(
                {"status":"ERROR","ERROR":str(e)}
            )
        
class ConfirmationViewset(viewsets.ModelViewSet):
    def create(self,request):
        try:
            if len(request.body) > 0:
                output_dict = json.loads(request.body.decode("utf-8"))
                data = dict()
                data['DOB'] = output_dict.get('DOB')
                data['issue'] = output_dict.get('issue')
                data['description'] = output_dict.get('description')
                data['date'] = output_dict.get('date')
                data['time'] = output_dict.get('time')


                # print(data)

                Confirmation_create = Confirmation(**data)
                Confirmation_create.save()

                return Response(
                    {"status":"OKAY","data":data}, status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"status":"ERROR","ERROR":str(e)}
            )
        
class Consultation_detailsViewset(viewsets.ModelViewSet):
    def create(self,request):
        try:
            if len(request.body) > 0:
                output_dict = json.loads(request.body.decode("utf-8"))
                data = dict()
                data['user_id'] = output_dict.get('user_id')
                data['therapist_name'] = output_dict.get('therapist_name')
                data['date_of_consultation'] = output_dict.get('date_of_consultation')
                data['description_by_therapist'] = output_dict.get('description_by_therapist')


                # print(data)

                Consultation_details_create = Consultation_details(**data)
                Consultation_details_create.save()

                return Response(
                    {"status":"OKAY","data":data}, status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"status":"ERROR","ERROR":str(e)}
            )
# class loginViewset(viewsets.ModelViewSet):
#     def create(self,request):
#         try:
#             if len(request.body) > 0:
#                 output_dict = json.loads(request.body.decode("utf-8"))
#                 data = dict()
#                 data['email_address'] = output_dict.get('email_address')
#                 data['login_password'] = output_dict.get('login_password')
                
#                 # print(data)

#                 login_create = login(**data)
#                 login_create.save()

#                 return Response(
#                     {"status":"OKAY","data":data}, status=status.HTTP_201_CREATED
#                 )
#         except Exception as e:
#             return Response(
#                 {"status":"ERROR","ERROR":str(e)}
#             )
# # Create your views here.
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset=Company.objects.all()
#     serializer_class=CompanySerializer

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
