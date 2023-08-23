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

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(updated_by=self.request.user)

    
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyEmployeeList(generics.ListCreateAPIView):
    queryset = CompanyEmployee.objects.all()
    serializer_class = CompanyEmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CompanyEmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyEmployee.objects.all()
    serializer_class = CompanyEmployeeSerializer


class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class DelegationList(generics.ListCreateAPIView):
    queryset = Delegation.objects.all()
    serializer_class = DelegationSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class DelegationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delegation.objects.all()
    serializer_class = DelegationSerializer