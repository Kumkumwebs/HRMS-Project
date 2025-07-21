from django.urls import path
from . import views

urlpatterns = [
    # Public pages
    path('', views.home_view, name='home'),

    # User dashboard (for logged-in users)
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Employee leave request form
    path('leave-request/', views.leave_request_view, name='leave_request'),

    # HR/Admin: Approve or reject leave requests
    path('leave-approval/', views.leave_approval_view, name='leave_approval'),

    # HR/Admin: View all leave request summaries
    path('leave-dashboard/', views.leave_dashboard_view, name='leave_dashboard'),
    
    path('profile/', views.employee_profile_view, name='profile'),

    path('attendance/', views.attendance_view, name='attendance'),

    path('admin-attendance/', views.admin_attendance_view, name='admin_attendance'),
 
    path('performance/', views.performance_view, name='performance'),
    
    path('employee-login/', views.employee_login_view, name='employee_login'),

    path('hr-dashboard/', views.hr_dashboard_view, name='hr_dashboard'),

    path('hr-login/', views.hr_login_view, name='hr_login'),

    path('my-leaves/', views.my_leave_summary_view, name='my_leave_summary'),

]
    







