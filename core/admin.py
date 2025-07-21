from django.contrib import admin
from .models import EmployeeProfile, Attendance, LeaveRequest, Performance

admin.site.register(EmployeeProfile)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)
admin.site.register(Performance)
