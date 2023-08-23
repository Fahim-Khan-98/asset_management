from django.shortcuts import render
from asset_app.models import Company, CompanyEmployee, Asset, Delegation
from asset_app.serializers import CompanySerializer,CompanyEmployeeSerializer,DelegationSerializer,AssetSerializer
from rest_framework import generics


# Create your views here.
def home(request):
    return render(request, 'asset_app/home.html')


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyEmployeeList(generics.ListCreateAPIView):
    queryset = CompanyEmployee.objects.all()
    serializer_class = CompanyEmployeeSerializer


class CompanyEmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyEmployee.objects.all()
    serializer_class = CompanyEmployeeSerializer


class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class DelegationList(generics.ListCreateAPIView):
    queryset = Delegation.objects.all()
    serializer_class = DelegationSerializer

class DelegationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delegation.objects.all()
    serializer_class = DelegationSerializer