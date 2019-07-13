from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import ProfileForm
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        context={}
        isType = request.POST.get('isType')
        # return render(request,'users/check.html',{'isType':isType})
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            u = user_form.save(commit=False)
            p = profile_form.save(commit = False)
            u.save()
            p.user = u
            p.save()
            p1 = Profile.objects.get(id=p.id)
            if isType == 'Wholesaler':
                p1.is_whole = True
                p1.save()
            elif isType == 'Retailer':
                p1.is_retail = True
                p1.save()

            context['p'] = p1
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return HttpResponseRedirect('/login/')
            # return render(request,'users/check.html',context)
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html', { 'user_form':user_form, 'profile_form':profile_form})


@login_required
def profile(request):
    return render(request,'users/profile.html')

# def auth_views(request):
#     username = request.POST.get('username','')
#     password = request.POST.get('password','')
#
#     user = auth.authenticate(username = username, password = password)
#
#     if user is not None:
#         if user.is_active:
#             auth.login(request, user)
#             if request.user.profile.is_whole:
#                 return render(request,'/w/')
#             elif request.user.profile.is_retail:
#                 return render(request,'/r/')
#     else:
#         return HttpResponseRedirect("Invalid username or password")
