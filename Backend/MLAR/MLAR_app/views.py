from django.shortcuts import render

# Create your views here.
# !!!---------------- Applicants -------------------------------------------------!!!

#============================
#== Home Page ===============
#============================
def index(request):
    dynamic_stuff = "Whore Iceland"
    context = {    # Add dynamic stuff here
        'dynamic_stuff':dynamic_stuff,
    }
    return render(request,"index.html", context)

