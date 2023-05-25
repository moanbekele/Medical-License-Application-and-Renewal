"""
URL configuration for MLAR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include  
from MLAR_app.views import * #!!! Import views 
from django.conf import settings  #!!! Import settings
from django.conf.urls.static import static #!!! Import static files 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('select2/', include('django_select2.urls')),
    # !!! -------------- APPLICANTS ------------------------------------------------
    path('',index, name='home'), # Add index function to path
    # ---- Registration ------
    path('register/',register_new_applicants, name='register'),
    path('register-new-license/',register_new_license, name='new'),
    path('lost-License/',register_lost_applicants, name='lost'),
    path('renewal/',register_renewal_applicants, name='renewal'),
    # ---- Success -----------
    path('save-id/<str:ad>/',save_id, name='save_id'),
    path('registration-success/',registration_success, name='reg_success'),
    path('lost-License-success/',lost_License_success, name='lost_success'),
    path('renewal-success/',renewal_success, name='renew_success'),

    # !!! -------------- DASHBOARD ------------------------------------------------
    path('dashboard/',dashboard_verify, name='dashboard'),
    path('dashboard/accepted',dashboard_accepted, name='accepted'),
    path('dashboard/denied',dashboard_denied, name='denied'),
    path('dashboard/notify',dashboard_notify, name='notify'),
    path('dashboard/verify',dashboard_verify, name='verify'),
    path('dashboard/verify-check/<str:fr>/<str:type>/<str:ve>',checker_verify, name='checker'),
    # ---- Authentication -----------
    path('login/',loginpage, name='login'),
    path('logout/',logoutuser, name='logout'),
    path('signup/',registerPage, name='signup'),
    path('forgot-password/',forgot_password, name='forgot_pass'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Static files
