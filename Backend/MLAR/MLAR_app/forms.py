from django.forms import ModelForm
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#---- DRYS ----
dropdown = {
            'type':'text',
            'class':'custom'
            }

serial_num = {
            'type':'text',
            'placeholder':'Put in your serial Number'
            }
health_profession = {
            'type':'text',
            'list':'health-professions', 
            'placeholder':'--Select health profession--'
            }
img_field = {
            'required':'required'
            }



class First_License_ApplicationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['applicant'].widget.attrs.update(dropdown)
        self.fields['id_serial_no'].widget.attrs.update(serial_num)
        self.fields['health_profession'].widget.attrs.update(health_profession)
        self.fields['grade_8th_ministry'].widget.attrs.update(img_field)
        self.fields['grade_10th_ministry'].widget.attrs.update(img_field)
        self.fields['grade_12th_ministry'].widget.attrs.update(img_field)
        self.fields['degree_certificate'].widget.attrs.update(img_field)
        self.fields['recent_photo'].widget.attrs.update(img_field)

    class Meta:
        model = First_License_Application
        fields =  ['applicant','id_serial_no','health_profession','grade_8th_ministry','grade_10th_ministry','grade_12th_ministry','degree_certificate','recent_photo']


class Regain_lost_licenseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['applicant'].widget.attrs.update(dropdown)
        self.fields['first_license'].widget.attrs.update(dropdown)
        self.fields['id_serial_no'].widget.attrs.update(serial_num)
        self.fields['recent_photo'].widget.attrs.update(img_field)

    class Meta:
        model = Regain_lost_license
        fields =  ['applicant','first_license','id_serial_no','recent_photo']


class Renew_last_licenseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['applicant'].widget.attrs.update(dropdown)
        self.fields['first_license'].widget.attrs.update(dropdown)
        self.fields['id_serial_no'].widget.attrs.update(serial_num)
        self.fields['old_license'].widget.attrs.update(img_field)
        self.fields['recent_photo'].widget.attrs.update(img_field)

    class Meta:
        model = Renew_last_license
        fields =  ['applicant','first_license','id_serial_no','old_license','recent_photo']

# ----------- Authentication ------------
class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                'class': 'form-control',
                'type':'text',
                'id':'username',
                'placeholder':'Enter your username',
                'autofocus':'autofocus'
                })
            
            self.fields['email'].widget.attrs.update({
                'class': 'form-control',
                'type':'text',
                'id':'email',
                'placeholder':'Enter your email'
                })
            
            self.fields['password1'].widget.attrs.update({
                'type':'password',
                'id':'password',
                'class':'form-control',
                'placeholder':'........',
                'aria-describedby':'password'
                })
            
            self.fields['password2'].widget.attrs.update({
                'type':'password',
                'id':'password',
                'class':'form-control',
                'placeholder':'........',
                'aria-describedby':'password'
                })

    class Meta:
        model = User
        fields = ['username','email','password1','password2']