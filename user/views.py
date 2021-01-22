from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import UserForm,FormUser
from .models import Usercostumer
# Create your views here.


def logoutUser(request):
    logout(request)
    return redirect("user:login")

def userlogin(request):
    form = UserForm()
    context = {
        "form": form
    }

    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat:index')
            else:
                return render(request, 'user/login.html', {'errorLogin': True})

        elif request.POST.get('submit') == 'sign_up':
            form = FormUser(request.POST)
            if form.is_valid():
                user = form.save()
                return render(request, 'user/login.html')

            else:
                return render(request, 'user/login.html', {'error': True})
        else:
            return render(request, 'user/login.html', {'error': True})

    return render(request, 'user/login.html', context)



def settingProfil(request):
    users = request.user.usercostumer
    form = FormUser(instance=users)
    profil = Usercostumer.objects.get(user=request.user)
    
    if request.method == "POST":
        form = FormUser(request.POST, request.FILES, instance=users)
        if form.is_valid():
            form.save()
            context = {
                "profil": profil,
                'form': form,
            }
            return redirect("user:setting")

    context = {
        "profil": profil,
        'form': form,
    }
    return render(request, 'user/setting.html', context)
