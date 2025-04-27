from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import LeaveRequest
from datetime import date
#from .forms import EmployeeProfileForm
#from django.contrib import messages


# ------------------------------
# Public and Dashboard Views
# ------------------------------

def home_view(request):
    return render(request, "core/home.html")

@login_required
def dashboard_view(request):
    return render(request, "core/dashboard.html")

# ------------------------------
# Leave Request View (Employee)
# ------------------------------

@login_required
def leave_request_view(request):
    if request.method == "POST":
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']

        LeaveRequest.objects.create(
            employee=request.user,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status="Pending"
        )

        return render(request, "core/leave_request.html", {"message": "Leave request submitted!"})

    return render(request, "core/leave_request.html")

# ------------------------------
# Leave Approval View (HR/Admin)
# ------------------------------

@staff_member_required
def leave_approval_view(request):
    if request.method == "POST":
        req_id = request.POST["request_id"]
        action = request.POST["action"]
        leave = LeaveRequest.objects.get(id=req_id)

        if action == "approve":
            leave.status = "Approved"
        elif action == "reject":
            leave.status = "Rejected"

        leave.save()

    pending = LeaveRequest.objects.filter(status="Pending")
    return render(request, "core/leave_approval.html", {"leave_requests": pending})

# ------------------------------
# Leave Dashboard (Summary View)
# ------------------------------

@staff_member_required
def leave_dashboard_view(request):
    leave_requests = LeaveRequest.objects.all().order_by('-date')

    count_approved = leave_requests.filter(status="Approved").count()
    count_rejected = leave_requests.filter(status="Rejected").count()
    count_pending = leave_requests.filter(status="Pending").count()
    total = leave_requests.count()

    return render(request, "core/leave_dashboard.html", {
        "leave_requests": leave_requests,
        "count_approved": count_approved,
        "count_rejected": count_rejected,
        "count_pending": count_pending,
        "total": total
    })
from .models import EmployeeProfile

@login_required
def employee_profile_view(request):
    try:
        profile = EmployeeProfile.objects.get(user=request.user)
    except EmployeeProfile.DoesNotExist:
        
        profile = None

    return render(request, "core/profile.html", {"profile": profile})


from .models import Attendance

@login_required
def attendance_view(request):
    message = ""
    if request.method == "POST":
        status = request.POST.get("status")
        already_marked = Attendance.objects.filter(employee=request.user, date=date.today()).exists()
        
        if not already_marked:
            Attendance.objects.create(employee=request.user, status=status)
            message = "Attendance marked successfully!"
        else:
            message = "You already marked your attendance for today."

    today_attendance = Attendance.objects.filter(employee=request.user, date=date.today()).first()

    return render(request, "core/attendance.html", {
        "today_attendance": today_attendance,
        "message": message
    })


@staff_member_required
def admin_attendance_view(request):
    from django.db.models import Q
    from datetime import datetime

    # Optional date filter
    date_str = request.GET.get("date")
    if date_str:
        try:
            filter_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            records = Attendance.objects.filter(date=filter_date)
        except:
            records = Attendance.objects.all().order_by('-date')  # fallback
    else:
        records = Attendance.objects.all().order_by('-date')

    return render(request, "core/admin_attendance.html", {
        "records": records,
        "filter_date": date_str or ""
    })


from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('home')  # after logout, it will go to home page

from .models import Performance

@login_required
def performance_view(request):
    performance_data = Performance.objects.filter(employee=request.user).order_by('-date')

    return render(request, "core/performance.html", {
        "performance_data": performance_data
    })

from django.contrib.auth import authenticate, login

def employee_login_view(request):
    error_message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid username or password."

    return render(request, "core/employee_login.html", {
        "error_message": error_message
    })


from django.contrib.admin.views.decorators import staff_member_required
from .models import LeaveRequest, Attendance, EmployeeProfile

@staff_member_required
def hr_dashboard_view(request):
    leave_count = LeaveRequest.objects.count()
    attendance_count = Attendance.objects.count()
    employee_count = EmployeeProfile.objects.count()

    return render(request, "core/hr_dashboard.html", {
        "leave_count": leave_count,
        "attendance_count": attendance_count,
        "employee_count": employee_count,
    })

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def hr_login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('hr_dashboard')
        else:
            message = "Invalid login or not authorized as HR."

    return render(request, "core/hr_login.html", {"message": message})


from .models import LeaveRequest
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest, Attendance, EmployeeProfile


@login_required
def my_leave_summary_view(request):
    leave_requests = LeaveRequest.objects.filter(employee=request.user).order_by('-start_date')
    return render(request, "core/my_leave_summary.html", {
        "leave_requests": leave_requests
    })

#def employees_add(request):
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees_all') 
    else:
        form = EmployeeProfileForm()
    return render(request, 'core/employees_add.html', {'form': form})
    
#def employees_all(request):
    from .models import EmployeeProfile
    employees = EmployeeProfile.objects.all()
    return render(request, 'employee_all.html', {'employees': employees})

#def create_user(request):
    if request.method == "POST":
        # Get the data from the form
        username = request.POST['username']
        password = request.POST['password']

        # Create the user with the provided username and password
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            messages.success(request, "User created successfully.")
            return redirect('home')  # Redirect to home or another page
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return render(request, 'core/create_user.html')

    return render(request, 'core/create_user.html')




