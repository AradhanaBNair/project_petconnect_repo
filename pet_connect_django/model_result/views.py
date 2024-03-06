from django.shortcuts import render


def home(request):
    return render(request, 'PetCareConnect/index.html')

