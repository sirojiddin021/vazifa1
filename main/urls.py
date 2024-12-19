from django.urls import path
from .views import index_view, about_view, contact_view, service_view, success
urlpatterns = [
    path('', index_view, name='index'), 
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('services/', service_view, name='services'),
    path('success/', success, name='success'),
]