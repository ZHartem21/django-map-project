# views.py
from django.shortcuts import render


def start_page(request):
    return render(request, 'start_page.html')