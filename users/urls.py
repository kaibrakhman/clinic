from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='sing_in.html'), name='sign_in'),
    path('logout/', LogoutView.as_view(), name='sign_out'),
    path('sign_up/', views.sign_up_view, name='sig_up')
]