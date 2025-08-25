from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    try:
        notes = Notes.objects.filter(owner=request.user)
        data = {'notes' : notes}

        return render(request, 'Main/index.html', data)
    except:
        return redirect('login')
    
def note(request, number):
    notes = Notes.objects.filter(id=number)
    data = {'notes' : notes, 
            'id': number}
    if request.method == "POST":
        if 'delete' in request.POST:
            notes.delete()
            return redirect('home')
    return render(request, f'Main/page.html', data)

def create(request):
    forms = NotesForm()
    data = {'forms' : forms, 'btn': 'Добавить'}
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)     
            note.owner = request.user         
            note.save() 
            return redirect('home')
        else:
            pass

    return render(request, 'Main/createpage.html', data)

def edit(request, number):
    forms = NotesForm()
    note = get_object_or_404(Notes, id=number)
    data = {'forms' : forms, 'btn': 'Изменить'}
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()     
            return redirect('home')
        else:
            pass

    return render(request, 'Main/createpage.html', data)

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    
    return render(request, 'Main/login.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Error")
    
    return render(request, 'Main/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'Main/about.html')