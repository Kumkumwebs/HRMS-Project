from django.contrib.auth.models import User
from django.db import models

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()

class Attendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(('Present', 'Present'), ('Absent', 'Absent')))

class LeaveRequest(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')))
    date = models.DateField(auto_now_add=True) 
class Performance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    remarks = models.TextField()
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)


