from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import Inance, Info, About, Services, Clients, Contact

# Create your views here.
def index_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        client = Contact(name=name, phone=phone, email=email, message=message)
        client.save()
        reverse('success')


    context = {
        'info' : Info.objects.first(),
        'inance' : Inance.objects.first(),
        'about' : About.objects.first(),
        'clients' : Clients.objects.all(),
        'contact' : Contact.objects.all(),
        'services' : Services.objects.all(),
    }
    return render(request, 'index.html', context)


def about_view(request):
    context = {
        'about' : About.objects.first(),
        'info' : Info.objects.first(),
    }
    return render(request, 'about.html', context)


def service_view(request):
    context = {
       'services' : Services.objects.all(),
        'info' : Info.objects.first(),
    }
    return render(request, 'service.html', context)


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        client = Contact(name=name, phone=phone, email=email, message=message)
        client.save()
        reverse_lazy('success')

    context = {
        'contact' : Contact.objects.all(),
        'info' : Info.objects.first(),
    }
    return render(request, 'contact.html', context)


def success(request):
    context = {
        'contact' : Contact.objects.first(),
    }
    return render(request, 'success.html', context)