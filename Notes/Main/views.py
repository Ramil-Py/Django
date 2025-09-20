from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    try:
        notes = Notes.objects.filter(owner=request.user)
        notes = notes[::-1]
        data = {'notes' : notes}

        return render(request, 'Main/index.html', data)
    except:
        return redirect('login')
    
def note(request, number):
    note = get_object_or_404(Notes, id=number)
    data = {'note' : note, 
            'id': number}
    if request.method == "POST":
        if 'delete' in request.POST:
            print("Error delete")
            note.delete()
            return redirect('home')
        else:
            print("Error delete")
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
            print("Error")
            pass

    return render(request, 'Main/createpage.html', data)

def edit(request, number):
    note = get_object_or_404(Notes, id=number)
    forms = NotesForm(instance=note)
    data = {'forms' : forms, 'btn': 'Изменить'}
    if request.method == "POST":
        forms = NotesForm(request.POST, instance=note)
        if forms.is_valid():
            note = forms.save()     
            return redirect('home')
        else:
            print(forms.errors)

    return render(request, 'Main/createpage.html', data)

def register(request):
    data = {
        'bool': True,
        'txt': 'Sign Up',
        'error': ''
    }
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 == password2:
            User.objects.create_user(username=username, password=password1)
            return redirect('login')
        else:
            data['error'] = 'Not the same'
    
    return render(request, 'Main/login.html', data)

def user_login(request):
    data = {
        'bool': False,
        'txt': 'Sign In',
        'error': '', 
    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            data['error'] = 'Incorrect data'
            print("Error")
    
    return render(request, 'Main/login.html', data)

def user_logout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'Main/about.html')