from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm

notes = Notes.objects.order_by('date')
data1 = {'notes' : notes}

forms = NotesForm()
data2 = {'forms' : forms}

def index(request):
    return render(request, 'Main/index.html', data1)

def note(request, id):
    return render(request, f'Main/page{str(id)}.html')

def create(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            pass

    return render(request, 'Main/createpage.html', data2)

def about(request):
    return render(request, 'Main/about.html')