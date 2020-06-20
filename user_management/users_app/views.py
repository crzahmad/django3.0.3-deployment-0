from django.shortcuts import render
from users_app.forms import UserForm,UserInfoForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def index(request):

    return render(request,'users_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        user1 = UserForm(data=request.POST)
        profile1 = UserInfoForm(data=request.POST)

        if user1.is_valid() and profile1.is_valid():

            user   =   user1.save()
            user.set_password(user.password)
            user.save()

            profile    =   profile1.save(commit=False)
            profile.user   =   user

            if 'propic' in request.FILES:
                profile.propic = request.FILES['propic']

            profile.save()

            registered = True

        else:
            print(user1.errors,profile1.errors)
    else:
        user1    =   UserForm()
        profile1 =   UserInfoForm()

    return render(request,'users_app/registration.html',{'user1':user1,'profile1':profile1,'registration':register})

def user_login(request):

    if request.method == 'POST':

        username    =   request.POST.get('username')
        password    =   request.POST.get('password')

        # django automated authentiacation!
        user    =   authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not ACTIVE!")
        else:
            print('Someone tried to login and failed XOXO!')
            print(f'Username:{username}/n Password:{password}')

    else:
        return render(request,'users_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def success(request):
    return render(request,'users_app/success.html')












# Create your views here.
