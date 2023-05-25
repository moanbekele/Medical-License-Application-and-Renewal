from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout  # Registration Login , Logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import json

from django.http import JsonResponse
# Create your views here.
# !!!---------------- Applicants START-------------------------------------------------!!!

#============================
#== Home Page ===============
#============================
def index(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Applicants/index.html", context)

#=================================
#== New Applicant Registration ===
#=================================
def register_new_applicants(request):
    
    if request.method == "POST":
        applicant = Applicant()
        applicant.first_name = request.POST.get('first_name')
        applicant.middle_name = request.POST.get('middle_name')
        applicant.last_name = request.POST.get('last_name') 
        applicant.gender = request.POST.get('gender')
        applicant.email = request.POST.get('email')
        applicant.phone = request.POST.get('phone')
        applicant.grad_university = request.POST.get('grad_university')
        applicant.birth_date = request.POST.get('birth_date')
        applicant.year_of_graduation = request.POST.get('year_of_graduation')
        
        applicant.save()
        return redirect('/save-id/'+ str(applicant.id))
    return render(request,"Applicants/Registration_Pages/Applicant_registration.html")


#=================================
#== New Applicant Registration ===
#=================================


def register_new_license(request):
    form = First_License_ApplicationForm(instance=First_License_Application.objects.first())
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
        term = request.GET.get('term')
        applicants = Applicant.objects.all().filter(title__icontains=term)
        return JsonResponse(list(applicants.values()), safe=False)
    
    if request.method == 'POST':
        form = First_License_ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/registration-success/')
    else:
        form = First_License_ApplicationForm()
    return render(request, 'Applicants/Registration_Pages/New_License_Applicant_Registration.html', {'form': form})
#=================================
#== Lost License Registration ====
#=================================
def register_lost_applicants(request):
    
    form = Regain_lost_licenseForm()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
        term = request.GET.get('term')
        applicants = Applicant.objects.all().filter(title__icontains=term)
        response_content = list(applicants.values())
        print(response_content)
        return JsonResponse(list(applicants.values()), safe=False)
    
    if request.method == 'POST':
        form = Regain_lost_licenseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/lost-License-success/')
    else:
        form = Regain_lost_licenseForm()
    return render(request, 'Applicants/Registration_Pages/Lost_License_Applicant_Registration.html', {'form': form})

#================================
#== Renewal Registration ========
#================================
def register_renewal_applicants(request):
    form = Renew_last_licenseForm(instance=Renew_last_license.objects.first())
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': 
        term = request.GET.get('term')
        applicants = Applicant.objects.all().filter(title__icontains=term)
        return JsonResponse(list(applicants.values()), safe=False)
    
    if request.method == 'POST':
        form = Renew_last_licenseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/renewal-success/')
    else:
        form = Renew_last_licenseForm()
    return render(request, 'Applicants/Registration_Pages/License_Renewal_Applicant_Registration.html', {'form': form})
    
# !!!---------------- Applicants END-------------------------------------------------!!!

# !!!---------------- Success (Applicants) START--------------------------------------------------!!!

#================================
#== Save ID  ========
#================================
def save_id(request, ad):
    applicant_unique = Applicant.objects.filter(id=ad) 
    applicant = Applicant.objects.all() 
    context = {    # Add dynamic stuff here
        'applicant_unique':applicant_unique,
        'applicant':applicant,
    }
    return render(request,"Applicants/Success_Pages/Copy_serial.html", context)

#================================
#== Registration Success ========
#================================
def registration_success(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Applicants/Success_Pages/Registeration_Success_Page.html", context)

#================================
#== Regain Success ==============
#================================
def lost_License_success(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Applicants/Success_Pages/Regain_Success_Page.html", context)

#================================
#== Renewal Success =============
#================================
def renewal_success(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Applicants/Success_Pages/Renewal_Success_Page.html", context)

# !!!---------------- Success (Applicants) END----------------------------------------------------!!!









# !!!---------------- Dashboard START--------------------------------------------------!!!

#================================
#== Dashboard Home =============
#================================
@login_required(login_url='login')
def dashboard_home(request):
    first_license = First_License_Application.objects.all()
    lost_license = Regain_lost_license.objects.all()
    renew_license = Renew_last_license.objects.all()
    context = {    # Add dynamic stuff here
        'first_license':first_license,
        'lost_license':lost_license,
        'renew_license':renew_license,
    }
    return render(request,"Dashboard/Verify_Applicants.html", context)

#================================
#== Accepted Applicants =========
#================================
@login_required(login_url='login')
def dashboard_accepted(request):
    first_license = First_License_Application.objects.all()
    lost_license = Regain_lost_license.objects.all()
    renew_license = Renew_last_license.objects.all()
    context = {    # Add dynamic stuff here
        'first_license':first_license,
        'lost_license':lost_license,
        'renew_license':renew_license,
    }
    return render(request,"Dashboard/Accepted_Applicants.html", context)

#================================
#== Denied Applicants ===========
#================================
@login_required(login_url='login')
def dashboard_denied(request):
    first_license = First_License_Application.objects.all()
    lost_license = Regain_lost_license.objects.all()
    renew_license = Renew_last_license.objects.all()
    context = {    # Add dynamic stuff here
        'first_license':first_license,
        'lost_license':lost_license,
        'renew_license':renew_license,
    }
    return render(request,"Dashboard/Denied_Applicants.html", context)

#================================
#== Notify Applicants ===========
#================================
def dashboard_notify(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Dashboard/Notify_Applicants.html", context)

#================================
#== Verify Applicants ===========
#================================
@login_required(login_url='login')
def dashboard_verify(request):
    first_license = First_License_Application.objects.all()
    lost_license = Regain_lost_license.objects.all()
    renew_license = Renew_last_license.objects.all()
    context = {    # Add dynamic stuff here
        'first_license':first_license,
        'lost_license':lost_license,
        'renew_license':renew_license,
    }
    return render(request,"Dashboard/Verify_Applicants.html", context)


#================================
#== Verify Applicants ===========
#================================
@login_required(login_url='login')
def checker_verify(request,fr,type,ve):
    if type == 'first':
        verification = First_License_Application.objects.get(id=ve)
        if request.method == "POST":
            verification.validation_status = request.POST.get('validation_status')
            verification.declination_reason = request.POST.get('declination_reason')
            verification.save()
            return redirect('/dashboard/'+ fr)
        context = {'verification':verification}
        return render(request,'#', context)
    
    elif type == 'lost':
        verification = Regain_lost_license.objects.get(id=ve)
        if request.method == "POST":
            verification.validation_status = request.POST.get('validation_status')
            verification.declination_reason = request.POST.get('declination_reason')
            verification.save()
            return redirect('/dashboard/'+ fr)
        context = {'verification':verification}
        return render(request,'#', context)
    
    elif type == 'renew':
        verification = Renew_last_license.objects.get(id=ve)
        if request.method == "POST":
            verification.validation_status = request.POST.get('validation_status')
            verification.declination_reason = request.POST.get('declination_reason')
            verification.save()
            return redirect('/dashboard/'+ fr)
        context = {'verification':verification}
        return render(request,'#', context)
# !!!---------------- Dashboard END----------------------------------------------------!!!

# !!!---------------- Authentication (Dashboard) START---------------------------------------------!!!
#================================
#== Dashboard Login =============
#================================
def loginpage(request):
    if request.user.is_authenticated: # If already logedin then redirect
        return redirect('/dashboard/verify')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                    login(request, user)
                    return redirect('/dashboard/verify')
            else:
                messages.info(request, 'Username or Password Incorrect')
                #return render(request,'dashboard/login.html', context)

        context = {}
    return render(request,"Dashboard/Authentication/Login.html", context)

#============================
#== Logout =============
#============================
def logoutuser(request):
    logout(request)
    return redirect('login')



#============================
#== Registration =============
#============================
def registerPage(request):
  # If registration is for loged ppl then get rid of the if statement
#   if request.user.is_authenticated:
#     return redirect('/dashboard/verify')
    
#   else:
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Created For | ' + user)
        return redirect('login') 
    context = {'form':form}
    return render(request,'Dashboard/Authentication/Register.html', context)



#================================
#== Forgot Password =============
#================================
def forgot_password(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Dashboard/Authentication/Forgot-Password.html", context)
# !!!---------------- AUTHENTICATION (Dashboard) END-----------------------------------------------!!!