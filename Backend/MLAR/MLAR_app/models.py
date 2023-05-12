from django.db import models
import uuid

# Create your models here.

#==============================================================================
# ==== Applicant  =================
class Applicant(models.Model):
  # Id
  id_serial_no = models.CharField(max_length=36, default=uuid.uuid4)
  # Character
  first_name = models.CharField(max_length=200, null=True)
  middle_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  gender = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=50, null=True)
  grad_university = models.CharField(max_length=100, null=True)
  # Date and time
  birth_date = models.DateField(null=True)
  year_of_graduation = models.CharField(max_length=50, null=True)
  # Date Applied
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
        return str(self.first_name + " "+ self.middle_name) 
  


#==============================================================================
# ====  New License Application   =================
class First_License_Application(models.Model):
  # Foreign Key
  applicant = models.ForeignKey(Applicant, null=True, on_delete=models.SET_NULL)
  # Character
  id_serial_no = models.CharField(max_length=36, null=True)
  health_profession = models.CharField(max_length=200, null=True)
  # Documents
  grade_8th_ministry = models.ImageField(null=True,blank=True, upload_to="main/grade_8th_ministry/")
  grade_10th_ministry = models.ImageField(null=True,blank=True, upload_to="main/grade_10th_ministry/")
  grade_12th_ministry = models.ImageField(null=True,blank=True, upload_to="main/grade_12th_ministry/")
  degree_certificate = models.ImageField(null=True,blank=True, upload_to="main/degree_certificate/")
  recent_photo = models.ImageField(null=True,blank=True, upload_to="main/recent_photo/")
  # Dropdown
  STATUS = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
  
  REASON = (
        ('Forgery', 'Forgery'),
        ('Low Quality Documents', 'Low Quality Documents'),
        ('Invalid Credentials', 'Invalid Credentials'),
    )
  validation_status = models.CharField(max_length=500, null=True, choices=STATUS, default="NOT VERIFIED" )
  declination_reason = models.CharField(max_length=500, null=True, choices=REASON, default="NOT DECLINED")
  # Date Applied
  date_issued = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
        return str(self.applicant.first_name + "  " + self.applicant.middle_name + " | " + self.health_profession)
  

#==============================================================================
# ====  Regain lost license   =================
class Regain_lost_license(models.Model):
  # Foreign Key
  applicant = models.ForeignKey(Applicant, null=True, on_delete=models.SET_NULL)
  first_license = models.ForeignKey(First_License_Application, null=True, on_delete=models.SET_NULL)
  # Character
  id_serial_no = models.CharField(max_length=36, null=True)
  # Documents
  recent_photo = models.ImageField(null=True,blank=True, upload_to="regain/recent_photo/")
  # Dropdown
  STATUS = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
  
  REASON = (
        ('Forgery', 'Forgery'),
        ('Low Quality Documents', 'Low Quality Documents'),
        ('Invalid Credentials', 'Invalid Credentials'),
    )
  validation_status = models.CharField(max_length=500, null=True, choices=STATUS, default="NOT VERIFIED" )
  declination_reason = models.CharField(max_length=500, null=True, choices=REASON, default="NOT DECLINED")
  # Date Applied
  date_issued = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
        return str(self.applicant.first_name + "  " + self.applicant.middle_name + " | " + self.first_license.health_profession)

#==============================================================================
# ====  Renew last license   =================
class Renew_last_license(models.Model):
  # Foreign Key
  applicant = models.ForeignKey(Applicant, null=True, on_delete=models.SET_NULL)
  first_license = models.ForeignKey(First_License_Application, null=True, on_delete=models.SET_NULL)
  # Character
  id_serial_no = models.CharField(max_length=36, null=True)
  # Documents
  old_license = models.ImageField(null=True,blank=True, upload_to="renew/old_license/")
  recent_photo = models.ImageField(null=True,blank=True, upload_to="renew/recent_photo/")
  # Dropdown
  STATUS = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
  
  REASON = (
        ('Forgery', 'Forgery'),
        ('Low Quality Documents', 'Low Quality Documents'),
        ('Invalid Credentials', 'Invalid Credentials'),
    )
  validation_status = models.CharField(max_length=500, null=True, choices=STATUS, default="NOT VERIFIED" )
  declination_reason = models.CharField(max_length=500, null=True, choices=REASON, default="NOT DECLINED")
  # Date Applied
  date_issued = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
        return str(self.applicant.first_name + "  " + self.applicant.middle_name + " | " + self.first_license.health_profession)
  
#==============================================================================
# ====  Applications   =================
class Application(models.Model):
  # Foreign Key
  applicant = models.ForeignKey(Applicant, blank=True, null=True, on_delete=models.SET_NULL)
  first_license = models.ForeignKey(First_License_Application, blank=True, null=True, on_delete=models.SET_NULL)
  renew_license = models.ForeignKey(Regain_lost_license, blank=True, null=True, on_delete=models.SET_NULL)
  lost_license = models.ForeignKey(Renew_last_license, blank=True, null=True, on_delete=models.SET_NULL)
  def __str__(self):
        return str(self.applicant.first_name + " "+ self.applicant.middle_name )
  

#==============================================================================
# ====  Employee   =================
class Employee(models.Model):
  # Character
  employee_name = models.CharField(max_length=500, null=True)
  employee_position = models.CharField(max_length=500, null=True)
  # Date Applied
  date_issued = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
        return str(self.employee_name)

#==============================================================================
# ====  Validation   =================
class Validate(models.Model):
  # Foreign Key
  application = models.ForeignKey(Application, null=True, on_delete=models.SET_NULL)
  # Many to Many
  employee = models.ManyToManyField(Employee)
  
  # Dropdown
  STATUS = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
  
  REASON = (
        ('Forgery', 'Forgery'),
        ('Low Quality Documents', 'Low Quality Documents'),
        ('Invalid Credentials', 'Invalid Credentials'),
    )
  validation_status = models.CharField(max_length=500, null=True, choices=STATUS)
  # Character
  declination_reason = models.CharField(max_length=500, null=True, choices=REASON)
  # Date Applied
  date_issued = models.DateTimeField(auto_now_add=True, null=True)
  def __str__(self):
        return str(str(self.application) + " | " + self.validation_status)




