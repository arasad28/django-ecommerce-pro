from email import message
from telnetlib import AUTHENTICATION
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpRequest
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

# AUTHENTICATION 

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# forms and model 

from app_login.models import Profile
from app_login.forms import ProfileForm,Profile, SignupForm
from app_shop.models import Product

# message
from django.contrib import messages

# Create your views here.

# class MyProducts(LoginRequiredMixin,TemplateView):
#     template_name = 'app_login/myproducts.html'
@login_required
def my_product(request):
    if request.method == 'POST':
        pk = request.POST.get('prod_pk')
        item = Product.objects.get(pk=pk)
        item.q_deal_req = True
        item.save()

    return render(request,'app_login/myproducts.html')
def sign_up(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!')
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request,'app_login/signup.html',context={'form':form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_shop:home'))
    return render(request,'app_login/login.html',context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request,'You are logged out!')
    return HttpResponseRedirect(reverse('app_shop:home'))

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request,'Change Saved')
    return render(request,'app_login/profile_update.html',context={'form':form})
