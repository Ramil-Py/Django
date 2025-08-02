from django.shortcuts import render
from .models import Notes

notes = Notes.objects.order_by('date')
data = {'notes' : notes}

def index(request):
    return render(request, 'Main/index.html', data)

def note(request, id):
    return render(request, f'Main/page{str(id)}.html')

def about(request):
    return render(request, 'Main/about.html')