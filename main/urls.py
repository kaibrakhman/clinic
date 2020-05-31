from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('branch/<str:name>/', views.branch_view, name='branch_view'),
    path('doctor/<str:full_name>/', views.doctor_view, name='doctor_view'),
    path('statement/to/<str:full_name>/', views.statement_view, name='statement_view'),
    path('prices/', views.prices, name='prices_view')
]