from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver



class Company(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    address = models.TextField(max_length=250,blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_comapany', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True, editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_comapany', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    # Add other company-specific fields

    def __str__(self):
        return self.name

class CompanyEmployee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    date_joined = models.DateField(blank=True,null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_employees', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_employees', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    # Add other employee-related fields
# use getattr
    def __str__(self):
        return self.user.username

class Asset(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_asset', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_asset', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    # Rest of the fields as before

    def __str__(self):
        return self.name



class Delegation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CompanyEmployee, on_delete=models.CASCADE)
    checkout_condition = models.TextField(blank=True)
    return_condition = models.TextField(blank=True)
    # start_date = models.DateField(auto_now_add=True,blank=True)
    # end_date = models.DateField(blank=True)
    # checkout_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_delegation', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_delegation', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    # def save(self, *args, **kwargs):
    #     if not self.start_date and not self.end_date:
    #         self.start_date = self.asset.start_date
    #         self.end_date = self.asset.end_date
        
    #     super(Delegation, self).save(*args, **kwargs)


    # def __str__(self):
    #     return f"{self.assigned_to.employee}'s {self.asset.name} delegation"
    
