from django.shortcuts import render
from rest_framework import viewsets
# from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response
from api.models import Booking
from rest_framework import status
import json


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

                return Response(
                    {"status":"OKAY","data":data}, status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"status":"ERROR","ERROR":str(e)}
            )
# # Create your views here.
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset=Company.objects.all()
#     serializer_class=CompanySerializer

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
