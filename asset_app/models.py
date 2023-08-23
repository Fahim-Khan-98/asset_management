from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250,blank=True, null=True)
    # Add other company-specific fields

    def __str__(self):
        return self.name

class CompanyEmployee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other employee-related fields

    def __str__(self):
        return self.employee.username

class Asset(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(CompanyEmployee, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # Rest of the fields as before

    def __str__(self):
        return self.name

class Delegation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CompanyEmployee, on_delete=models.CASCADE)
    checkout_condition = models.TextField(blank=True)
    return_condition = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    checkout_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.start_date and not self.end_date:
            self.start_date = self.asset.start_date
            self.end_date = self.asset.end_date
        
        super(Delegation, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.assigned_to.employee}'s {self.asset.name} delegation"
    
