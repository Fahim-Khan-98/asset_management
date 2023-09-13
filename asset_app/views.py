from django.shortcuts import render
from asset_app.models import Company, CompanyEmployee, Asset, Delegation
from asset_app.serializers import CompanySerializer,CompanyEmployeeSerializer,DelegationSerializer,AssetSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q


# Create your views here.
def home(request):
    deligations = Delegation.objects.all()
    assets = Asset.objects.all()

    total_deligations = deligations.count()

    # q = request.GET.get('q')
    # company = Company.objects.filter(Q(name__icontains=q))
    context = {
        'deligations': deligations,
        'total_deligations':total_deligations,
        'assets':assets,
    }
    return render(request, 'asset_app/home.html', context)


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('name','address')



    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyEmployeeList(generics.ListCreateAPIView):
    queryset = CompanyEmployee.objects.all()
    serializer_class = CompanyEmployeeSerializer

    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('first_name','last_name', 'company__name','user__username')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CompanyEmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyEmployee.objects.all()
    serializer_class = CompanyEmployeeSerializer


class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class DelegationList(generics.ListCreateAPIView):
    queryset = Delegation.objects.all()
    serializer_class = DelegationSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class DelegationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delegation.objects.all()
    serializer_class = DelegationSerializer