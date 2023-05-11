from django.db import models

# Create your models here.

#==============================================================================
# ====  New License Application   =================
class New_License_Application(models.Model):
  # Character
  serial_no = models.CharField(max_length=200, null=True)
  first_name = models.CharField(max_length=200, null=True)
  middle_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  gender = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=50, null=True)
  grad_university = models.CharField(max_length=100, null=True)
  health_profession = models.CharField(max_length=200, null=True)
  # Date and time
  birth_date = models.DateTimeField(null=True)
  year_of_graduation = models.DateTimeField(null=True)
  # Documents
  grade_8th_ministry = models.ImageField(null=True,blank=True, upload_to="main/grade_8th_ministry/")
  grade_10th_ministry = models.ImageField(null=True,blank=True, upload_to="main/grade_10th_ministry/")
  grade_12th_ministry = models.ImageField(null=True,blank=True, upload_to="main/grade_12th_ministry/")
  degree_certificate = models.ImageField(null=True,blank=True, upload_to="main/degree_certificate/")
  recent_photo = models.ImageField(null=True,blank=True, upload_to="main/recent_photo/")
  # Date Applied
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  def _str_(self):
    return self.name
  

#==============================================================================
# ====  Regain lost license   =================
class regain_lost_license(models.Model):
  # Character
  serial_no = models.CharField(max_length=200, null=True)
  first_name = models.CharField(max_length=200, null=True)
  middle_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  gender = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=50, null=True)
  health_profession = models.CharField(max_length=200, null=True)
  # Date and time
  birth_date = models.DateTimeField(null=True)
  date_issued = models.DateTimeField(null=True)
  # Documents
  recent_photo = models.ImageField(null=True,blank=True, upload_to="regain/recent_photo/")
  # Date Applied
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  def _str_(self):
    return self.name

#==============================================================================
# ====  Renew lost license   =================
class renew_lost_license(models.Model):
  # Character
  serial_no = models.CharField(max_length=200, null=True)
  first_name = models.CharField(max_length=200, null=True)
  middle_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  gender = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=50, null=True)
  health_profession = models.CharField(max_length=200, null=True)
  grad_university = models.CharField(max_length=200, null=True)
  # Date and time
  birth_date = models.DateTimeField(null=True)
  date_issued = models.DateTimeField(null=True)
  # Documents
  old_license = models.ImageField(null=True,blank=True, upload_to="renew/old_license/")
  recent_photo = models.ImageField(null=True,blank=True, upload_to="renew/recent_photo/")
  # Date Applied
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  def _str_(self):
    return self.name

