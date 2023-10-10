from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import CompanySerializer,EmployeeSerializer
from api.models import Company,Employee


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
