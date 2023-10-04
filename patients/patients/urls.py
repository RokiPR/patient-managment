from django.contrib import admin
from django.urls import path, include, re_path
from App import views

urlpatterns = [
    # Native path to access the django admin
    path('admin/', admin.site.urls),

    # Path to access the front-end page
    path("", views.frontend, name="frontend"),

    # Path to login / logout
    path("login/", include('django.contrib.auth.urls')),

    # ------------------- BACKEND SECTION ------------------
    # Path to access the back-end page
    path("backend/", views.backend, name="backend"),

    # Path to add patient
    path("add-patient/", views.add_patient, name="add_patient"),

    # Path to access the patient individually
    path("patient/<str:patient_id>/", views.patient, name="patient"),

    # Path to edit patient
    path("edit_patient/", views.edit_patient, name="edit_patient"),

    # Path to show all patients
    path("show-all-patients/", views.show_all_patients, name="show_all_patients"),

    # Path to delete a patient
    path("delete-patient/<str:patient_id>", views.delete_patient, name="delete_patient"),

    # re_path(r'^static/(?P<path>.*)$', serve, {})
]
