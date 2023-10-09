from django.shortcuts import render

from .forms import Form


def home(request):
    form = Form()
    return render(request, 'home.html', {'form': form})
