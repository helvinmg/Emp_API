from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.emplist),
    path('employees/<int:pk>', views.empdetail)
]