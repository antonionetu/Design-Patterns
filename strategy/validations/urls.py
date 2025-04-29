from django.urls import path
from . import views


urlpatterns = [
    path('example/<int:user_id>/', views.example),
]
