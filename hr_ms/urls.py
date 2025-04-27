from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import custom_logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  
    path('logout/', custom_logout_view, name='logout'),  
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]
