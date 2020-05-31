from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from main import models
# Create your views here.


def sign_up_view(request):
    all_branches = models.Branch.objects.all()
    all_doctors = models.Doctor.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            return redirect('sig_up')
    else:
        form = UserCreationForm()
        return render(request, 'sign_up.html', {'form': form, 'all_branches': all_branches, 'all_doctors': all_doctors})