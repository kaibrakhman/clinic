from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.


def main_view(request):
    all_branches = models.Branch.objects.all()
    all_doctors = models.Doctor.objects.all()

    return render(request, 'main.html', {'all_branches': all_branches, 'all_doctors': all_doctors, 'user': request.user})


def branch_view(request, name):
    branch = models.Branch.objects.get(name=name)
    doctors = models.Doctor.objects.filter(branch__name=name)
    all_branches = models.Branch.objects.all()
    all_doctors = models.Doctor.objects.all()

    return render(request, 'branch.html', {'branch': branch, 'doctors': doctors, 'all_branches': all_branches,
                                           'all_doctors': all_doctors, 'user': request.user})


def doctor_view(request, full_name):
    doctor = models.Doctor.objects.get(full_name=full_name)
    branch = models.Branch.objects.get(doctor=doctor)
    times = models.Times.objects.filter(branch=branch)

    return render(request, 'doctor.html', {'doctor': doctor, 'branch': branch, 'times': times,
                                           'all_branches': models.Branch.objects.all(),
                                           'all_doctors': models.Doctor.objects.all(), 'user': request.user})


def statement_view(request, full_name):
    doctor = models.Doctor.objects.get(full_name=full_name)
    statement = None
    all_branches = models.Branch.objects.all()
    all_doctors = models.Doctor.objects.all()
    if request.GET:
        patient_name = request.GET.get('patient_name')
        phone_number = request.GET.get('phone_number')
        comment = request.GET.get('comment')
        if patient_name != '' and phone_number != '':
            statement = models.Statement.objects.get_or_create(patient_name=patient_name,
                                                               phone=phone_number, doctor=doctor,
                                                               comment=comment)
    return render(request, 'statement.html', {'doctor': doctor, 'statement': statement, 'all_branches': all_branches,
                                              'all_doctors': all_doctors, 'user': request.user})


def prices(request):
    all_branches = models.Branch.objects.all()
    all_doctors = models.Doctor.objects.all()
    return render(request, 'prices.html', {'all_branches': all_branches,
                                           'all_doctors': all_doctors, 'user': request.user})