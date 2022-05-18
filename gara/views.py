from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import *
from datetime import date
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect

@login_required(login_url='/view-request')
def tiep_nhan(request):
    enquiry=forms.TiepNhanForm()
    count = PhieuTiepNhan.objects.filter(date=date.today()).count()
    if count > 30: ##Cần sửa với tham số
        enquiries=PhieuTiepNhan.objects.all().filter(date=date.today())

        return render(request, 'gara/customerbase.html', {'enquiries': enquiries})

    if request.method=='POST':
        enquiry=forms.TiepNhanForm(request.POST)
        if enquiry.is_valid():
            enquiry_x=enquiry.save()
        return render(request, 'gara/customerbase.html', {'enquiries': enquiries})
    
    return render(request,'gara/customerbase.html',{'enquiry':enquiry})

def view_request(request):
    enquiries=PhieuTiepNhan.objects.all().filter(date=date.today())
    return render(request,'gara/customerbase.html', {'enquiries': enquiries})

def logout(request):
    return render(request,'gara/logout.html',{})

def home(request):
    return render(request, 'gara/home.html',{})

def sign_up(request):
    form = RegisterForm(request.POST or None)
    context = {'userForm': form}
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            username = request.POST['username']
            password = request.POST['password']
            lastname = request.POST['lastname']
            firstname = request.POST['firstname']
            password = request.POST['password']
            mobile = request.POST['mobile']
            emails = request.POST['emails']
            profile_pic = request.FILES['profile_pic']
            address = request.POST['address']
            # list = [form.cleaned_data['username'], form.cleaned_data['password']]
            Customer.objects.create(username=username, password=password, lastname=lastname,
                                    firstname=firstname, mobile=mobile, emails=emails, 
                                    address=address , profile_pic=profile_pic)
            user = User.objects.create_user(username=username, password=password, 
                                first_name=firstname, last_name=lastname, email=emails)
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
            # form.save(commit=False)
            # return reversed('customer-profile', kwargs={'username': username})
    return render(request, 'gara/customersignup.html', context)
@login_required(login_url='/login-customer')
def profile(request, username):
    cus = Customer.objects.get(username=username)
    profile_pic = "../" + cus.profile_pic.url
    print(profile_pic)
    context = {'customer': cus, 'username': username, 'picture': profile_pic}
    return render(request,'gara/trial.html', context)

def customer_login_view(request):
    form = AuthenticationForm()
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f'username {username} password {password}')
        print(form.is_valid())
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Log In sucessfully')
            return redirect(f'../customer-profile/{username}')
        else:
            messages.warning(request, 'Login failed! Please fill your account again.')
        
    context = {'form': form}
    return render(request, 'gara/customerlogin.html', context)
@login_required(login_url='/login-customer')
def customer_dashboard_view(request, username):
    cus = Customer.objects.get(username=username)
    profile_pic = '../' + cus.profile_pic.url
    context = {'customer': cus, 'username': username, 'picture': profile_pic}
    return render(request, 'gara/customer_dashboard.html', context)

@login_required(login_url='/login-customer')
def edit_customer_profile_view(request, username):
    customer = get_object_or_404(Customer, username=username)
    CustomerUpdate_Form = CustomerUpdateForm(instance=customer)
    picture = '../' + customer.profile_pic.url
    print(customer)
    if request.method=='POST':
        CustomerUpdate_Form = CustomerUpdateForm(request.POST, request.FILES, instance=customer)
        if CustomerUpdate_Form.is_valid():
            print('valid')
            customer = CustomerUpdate_Form.save()
            customer.save()
            return HttpResponseRedirect(f'../customer-profile/{username}')
    mydict={'customerForm':CustomerUpdate_Form, 'picture': picture}
    return render(request,'gara/edit_customer_profile.html',mydict)

@login_required(login_url='/login-customer')
def edit_customer_account_view(request, username):
    customer = get_object_or_404(Customer, username=username)
    CustomerUpdate_Account = CustomerUpdateAccount(instance=customer)
    user = User.objects.get(username=request.user.username)
    picture = '../' + customer.profile_pic.url
    print(customer)
    if request.method=='POST':
        CustomerUpdate_Account = CustomerUpdateAccount(request.POST ,instance=customer)
        if CustomerUpdate_Account.is_valid():
            print('valid')
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.save()
            customer = CustomerUpdate_Account.save()
            customer.save()
            return redirect(f'../login-customer')
    mydict = {'userForm':CustomerUpdate_Account, 'picture':picture}
    return render(request,'gara/edit_customer_account.html', mydict)