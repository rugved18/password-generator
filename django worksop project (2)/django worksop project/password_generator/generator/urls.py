from django.urls import path
from .views import generate_passwords, generate_aws_password, generate_amazon_password, index

urlpatterns = [
    path('', index, name='index'),
    path('generate/', generate_passwords, name='generate_passwords'),
    path('generate/aws/', generate_aws_password, name='generate_aws_password'),
    path('generate/amazon/', generate_amazon_password, name='generate_amazon_password'),
]
