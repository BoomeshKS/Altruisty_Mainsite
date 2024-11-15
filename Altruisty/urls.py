from django.urls import path
from . import views

app_name="altruisty"

urlpatterns=[
    path("services/",views.services,name="services"),
    path("details/<str:heading>/",views.DetailsPage,name="details"),
    path("",views.home,name="index"),
    path("about/",views.aboutus,name="about"),
    path("intern/",views.interns,name="intern"),
    path("verify/",views.verify,name="verify"),
    path("contact/",views.contact,name="contact"),
    path("e-learning/",views.studentform,name="E-learning"),
    path("mentor_registration/",views.mentorform,name="Mentorform"),
    path("startup_registration/",views.startupform,name="Startupform")
    ]