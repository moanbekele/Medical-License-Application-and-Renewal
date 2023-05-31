from django.test import SimpleTestCase
from django.urls import reverse  


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("home1"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "Applicants/index.html")



class Applicant_Registration_pageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "Applicants/Registration_Pages/Applicant_registration.html")


class RenewalpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "Dashboard/Authentication/Login.html")
