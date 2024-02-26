from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html')


def about(request):
    return render(request, template_name='about.html')


def contact(request):
    return render(request, template_name='contact.html')


def services(request):
    return render(request, template_name='service.html')


def guard(request):
    return render(request, template_name='guard.html')

# Create your views here.
