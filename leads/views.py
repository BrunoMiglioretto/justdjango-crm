from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Lead


def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "second_page.html", context)

