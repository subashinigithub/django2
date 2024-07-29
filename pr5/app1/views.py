from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import *
from.models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def student_login(r):
    if r.user.is_authenticated and not(r,user.is_staff):
        return redirect('dashboard')
    if r.method=='POST':
        form = studentloginform(r, r.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(r, username=username, password=password)
            if user is not None:
                login(r, user)
                return redirect('dashboard')
            else:
                 form.add_error(None, 'Invalid email or password.')
    else:
        form = studentloginform()
    return render(r, 'student.html', {'form': form})






        


def new1(r):
    return HttpResponse("abcd")
def workout(r):
    username=r.session.get('name')
    if username is not None:
        
        return render(r,"workout.html",{'name':username})
    else:
        return redirect('pg2')
def logout(r):
    if 'name' in r.session:
        del r.session['name']
    return redirect('pg2')
    

from django.shortcuts import render,redirect
from django.http import HttpResponse
""" def login(request):
    if request.method=='POST':
       
            username=request.cleaned_data['username']
            password=request.cleaned_data['password']
            if username=="admin" and password=="admin":
                 return redirect('') """
def login(request):
    username=request.session.get('name')

    if username is not None:
        return redirect("pg1")
    
    else:
        if request.method=='POST':
            print("form")
            forms=dataform(request.POST)
            print("form")
            
            if forms.is_valid():
                print("username")
                username=forms.cleaned_data['username']
                password=forms.cleaned_data['password']
                print(username,password)
                if password=="admin":
                    print("password")
                    request.session['name']=username
                    return redirect('pg1')
                else:
                 return redirect('set_cookie')
                
        else:
            forms=dataform()
            return render(request,'session.html',{'form':forms})
         


