from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', views.generate, name='generate'),  # Use views.generate
    path('', views.index, name='index'),  # Add this line
]
