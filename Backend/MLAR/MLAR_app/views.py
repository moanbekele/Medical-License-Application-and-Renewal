from django.shortcuts import render

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
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Applicants/Registration_Pages/New_License_Applicant_Registration.html", context)

#=================================
#== Lost License Registration ====
#=================================
def register_lost_applicants(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Applicants/Registration_Pages/Lost_License_Applicant_Registration.html", context)

#================================
#== Renewal Registration ========
#================================
def register_renewal_applicants(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Applicants/Registration_Pages/License_Renewal_Applicant_Registration.html", context)

# !!!---------------- Applicants END-------------------------------------------------!!!

# !!!---------------- Success (Applicants) START--------------------------------------------------!!!

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
def dashboard_home(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Dashboard/index.html", context)

#================================
#== Accepted Applicants =========
#================================
def dashboard_accepted(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Dashboard/Accepted_Applicants.html", context)

#================================
#== Denied Applicants ===========
#================================
def dashboard_denied(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
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
def dashboard_verify(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Dashboard/Verify_Applicants.html", context)
# !!!---------------- Dashboard END----------------------------------------------------!!!

# !!!---------------- Authentication (Dashboard) START---------------------------------------------!!!
#================================
#== Dashboard Login =============
#================================
def login(request):
    dynamic_stuff = "dummy"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Dashboard/Authentication/Login.html", context)

#================================
#== Dashboard signup ============
#================================
def register(request):
    dynamic_stuff = "dummy"  
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"Dashboard/Authentication/Register.html", context)

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