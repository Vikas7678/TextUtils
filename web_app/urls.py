from django.urls import path
from . import views

urlpatterns = [
    path('', views.Analyze_text),
    path('textutils', views.textutils)
]
