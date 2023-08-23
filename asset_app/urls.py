from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from asset_app import views


urlpatterns = [
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),

    path('employee/', views.CompanyEmployeeList.as_view()),
    path('employee/<int:pk>/', views.CompanyEmployeeDetail.as_view()),

    path('asset/', views.AssetList.as_view()),
    path('asset/<int:pk>/', views.AssetDetail.as_view()),

    path('delegation/', views.DelegationList.as_view()),
    path('delegation/<int:pk>/', views.DelegationDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
