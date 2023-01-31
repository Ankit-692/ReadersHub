from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from googleapiclient.discovery import build
from .models import Book
from django.contrib import messages
import os

from dotenv import load_dotenv
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv()


def SignUp(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                userName = form.cleaned_data['UserName']
                f_name = form.cleaned_data['firstName']
                l_name = form.cleaned_data['lastName']
                Email = form.cleaned_data['Email']
                pass1 = form.cleaned_data['password1']
                pass2 = form.cleaned_data['password2']
                if pass1!=pass2:
                    return render(request, 'Sign Up.html', {'form': form, 'Perror': True})
                else:  
                    try:
                        user = User.objects.create_user(username = userName, first_name = f_name, last_name = l_name, password = pass1, email = Email)
                        user.save()
                        return redirect('/')
                    except IntegrityError:
                        return render(request, 'Sign Up.html', {'form': form, 'Ierror': True})

        else:
            form = SignUpForm()
        return render(request, 'Sign Up.html', {'form': form})

def SignIn(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        form = AuthenticationForm(data=request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('home')
            else:
                form = AuthenticationForm(data = request.POST)
                return render(request, 'Sign In.html', {'form': form, 'error': True})
        return render(request, 'Sign In.html', {'form':form})

def LogOut(request):
    if(request.method=='POST'):
        logout(request)
        return redirect('SignIn')

@login_required(login_url="SignIn")
def home(request):
    return render(request, 'home.html')

@login_required(login_url="SignIn")
def userList(request,state = ""):
    if state=="":
        books = Book.objects.filter(username = request.user)
    else:
        books = Book.objects.filter(username = request.user, state = state)
    return render(request, 'userList.html',{'data' : books})
    
@login_required(login_url="SignIn")
def search(request):
    API_KEY = str(os.getenv('Api_key'))
    print(API_KEY)
    service = build('books', 'v1', developerKey = API_KEY)
    if request.method == "GET":
        query = request.GET['Book']
        if(not query):
            return redirect('home')
        req = service.volumes().list(q = query, maxResults=40)
        response = req.execute()
        if response['totalItems'] != 0:
            return render(request,'results.html',{'response': response['items'], 'title':query})
        else:
            return render(request, 'notfound.html')

    if request.method == "POST":
        query = request.POST['Book']
        titleName = request.POST['titleName']
        description = request.POST['description']
        authors = request.POST['authors']
        totalPage = request.POST['totalPage']
        ratings = request.POST['ratings']
        imageLink = request.POST['imageLink']
        date = request.POST['date']
        book = Book(username = request.user.get_username(),
                     titleName = titleName,
                     description = description,
                     authors = authors,
                     totalPage = totalPage,
                     ratings = ratings,
                     image = imageLink,
                     publishedDate = date)
        book.save() 
        req = service.volumes().list(q = query, maxResults=40)
        response = req.execute()
        messages.success(request, 'Selected Book Added to Library')
        return redirect(f'/search?Book={query}')
        
@login_required(login_url="SignIn")
def update(request,id):
    book = Book.objects.get(id=id, username = request.user)
    if request.method == 'GET':
        return render(request, 'update.html',{'book':book})
    elif request.method == 'POST':
        book.pageRead = request.POST['pageRead']
        book.state = request.POST['state']
        book.save()
        return render(request, 'update.html',{'book':book, 'trr' : True})

@login_required(login_url="SignIn")
def delete(request,id):
    Book.objects.get(id = id).delete()
    return redirect('/user')
