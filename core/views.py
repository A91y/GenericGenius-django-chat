from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login



def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        myuser = User.objects.create_user(username= username, password=password)
        myuser.save()
        print(myuser)
        print("Done")
        login(request, myuser)
        return redirect('/')
    else:
        return render(request, 'registration/register.html')