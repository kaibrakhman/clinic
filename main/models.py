from django.db import models
from django.urls import reverse
# Create your models here.


class Days(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('branch_view', args=[self.name])


class Times(models.Model):
    start_t = models.CharField(max_length=10, default='')
    finish_t = models.CharField(max_length=10, default='')
    start_l = models.CharField(max_length=10, default='')
    finish_l = models.CharField(max_length=10, default='')
    day = models.ForeignKey(Days, on_delete=models.CASCADE, related_name='times')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='times')

    def __str__(self):
        return self.branch.name + ' ' + self.day.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=100, default='')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    rank = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True)
    price = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('doctor_view', args=[self.full_name])


class Statement(models.Model):
    patient_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.patient_name + ' - ' + self.doctor.full_name