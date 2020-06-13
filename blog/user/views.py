from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import userupdateForm,profielupdateForm
from django.contrib.auth.decorators import login_required

# User registeration form 
def register(request):
    if request.method == 'POST':
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=f_name,last_name=l_name,username=username,email=email,password=password1)
                user.save()
                return redirect('/')
        else:
            messages.error(request,'password does not match')
            return redirect('register')
    else:
        return render(request,'register.html')

# User login form
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')


    else:
        return render(request,'login.html')

# User logout form
def logout(request):
    auth.logout(request)
    return redirect('/')


# User profile details and update profile form
@login_required
def profile(request):
    if request.method == 'POST':
        u_form=userupdateForm(request.POST,instance=request.user)
        p_form=profielupdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Profile updated')
            return redirect('profile')
    
    else:
        u_form=userupdateForm(instance=request.user)
        p_form=profielupdateForm(instance=request.user.profile) 

        context = {
            'u_form':u_form,
            'p_form':p_form
        }

        return render(request,'profile.html',context)