from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index' ),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'), # overwrite the default
                                                                #  form of the generic LoginView with  custom one
    path('logout/',auth_views.LogoutView.as_view(),name='logout')                                                                
]
