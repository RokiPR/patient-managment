from django.shortcuts import render

# My Imports
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models.functions import Lower


# Function to render the frontend page
def frontend(request):
    return render(request, "frontend.html")

# ------------------- BACKEND SECTION ------------------
# Function to render the backend page

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) |
            Q(age__icontains=q) | Q(gender__icontains=q) | Q(note__icontains=q)
            ).order_by(Lower('name'))
        if not all_patient_list:
            return render(request, "backend.html", {"error_message": True})
    else:
        all_patient_list = Patient.objects.all().order_by(Lower('name'))
    
    paginator = Paginator(all_patient_list, 10)
    page = request.GET.get("page")
    all_patients = paginator.get_page(page)
    db_patients = Patient.objects.all()

    return render(request, "backend.html", {"patients": all_patients, 
                                            "db_patients": db_patients})


# Function to insert new patient

@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_patient(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        note = request.POST.get('note')
        # if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
        if name and phone and email and age and gender or note:
            patient = Patient()
            patient.name = name
            patient.phone = phone
            patient.email = email
            patient.age = age
            patient.gender = gender
            patient.note = note
            patient.save()
            messages.success(request, "Patient Added Successfully!")
            return HttpResponseRedirect("/backend")
    else:
        return render(request, "add.html")


# Function to access the patient individually

@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if patient:
        return render(request, "edit.html", {"patient": patient})

# Function to edit the patient
@login_required(login_url="login")
def edit_patient(request):
    if request.method == "POST":
        patient = Patient.objects.get(id=request.POST.get('id'))
        if patient:
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient Updated Successfully!")
            return HttpResponseRedirect("/backend")
        
# Function to show all patients
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def show_all_patients(request):
    all_patients = Patient.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) |
            Q(age__icontains=q) | Q(gender__icontains=q) | Q(note__icontains=q)
            ).order_by(Lower('name'))
        if not all_patient_list:
            return render(request, "backend.html", {"error_message": True})
    else:
        all_patient_list = Patient.objects.all().order_by(Lower('name'))

    return render(request, "show-all-patients.html", {"patients": all_patients})

# Function to Delete a patient
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, "Patient Removed Successfully!")
    return HttpResponseRedirect("/backend")