from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from datetime import date
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from imp import C_BUILTIN

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
def is_staff(user):
    return user.groups.filter(name='STAFF').exists()

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

@user_passes_test(is_admin)
@login_required(login_url='/login')
def createStaffAccount(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
            print('valid')
            username = request.POST['username']
            password = request.POST['password']
            lastname = request.POST['lastname']
            firstname = request.POST['firstname']
            password = request.POST['password']
            mobile = request.POST['mobile']
            emails = request.POST['emails']
            profile_pic = request.FILES['profile_pic']
            address = request.POST['address']
            Staff.objects.create(username=username, password=password, lastname=lastname,
                                    firstname=firstname, mobile=mobile, emails=emails, 
                                    address=address , profile_pic=profile_pic)
            user = User.objects.create_user(username=username, password=password, 
                                first_name=firstname, last_name=lastname, email=emails)
            user.is_staff = True
            user.save()
            my_customer_group = Group.objects.get_or_create(name='STAFF')
            my_customer_group[0].user_set.add(user)
            messages.success(request, f'Add staff {username} successfully! !!')
        else:
            messages.warning(request,'Invalid form, please filling a again!')
    context = {'userForm': form, 'username':request.user.username}
    return render(request, 'profile/create_new_staff.html', context)


@login_required(login_url='/login')
def profile(request, username):
    try:
        cus = Staff.objects.get(username=username)
        profile_pic = '../' + cus.profile_pic.url
        print(profile_pic)
    except:
        password = request.user.password
        cus = Staff.objects.create(username=username, password=password)
        cus.is_admin = True
        profile_pic = "../static/profile_pic/CustomerProfilePic/images.jpg"
        cus.profile_pic = profile_pic
        user = User.objects.get(username=username, password=password)
        user.save()
        my_customer_group = Group.objects.get_or_create(name='ADMIN')
        my_customer_group[0].user_set.add(user)
        cus.save()

    context = {'customer': cus, 'username': username, 'picture': profile_pic}
    return render(request,'profile/Profile.html', context)

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
            return redirect(f'../profile/{username}')
        else:
            messages.warning(request, 'Đăng nhập thất bại! Kiểm tra thông tin của bạn và đăng nhập lại')
    context = {'form': form}
    return render(request, 'profile/customerlogin.html', context)

@login_required(login_url='/login')
def customer_dashboard_view(request, username):
    cus = Staff.objects.get(username=username)
    profile_pic = '../' + cus.profile_pic.url
    context = {'customer': cus, 'username': username, 'picture': profile_pic}
    return render(request, 'profile/customer_dashboard.html', context)

@login_required(login_url='/login')
def edit_customer_profile_view(request, username):
    staff = get_object_or_404(Staff, username=username)
    staffUpdate_form = StaffUpdateForm(instance= staff)
    picture = '../' + staff.profile_pic.url
    print(staff)
    if request.method=='POST':
        staffUpdate_form = StaffUpdateForm(request.POST, request.FILES, instance=staff)
        if staffUpdate_form.is_valid():
            print('valid')
            staff = staffUpdate_form.save()
            staff.save()
            return HttpResponseRedirect(f'../profile/{username}')
    mydict={'customerForm':staffUpdate_form, 'picture': picture}
    return render(request,'profile/edit_customer_profile.html',mydict)

@login_required(login_url='/login')
def edit_customer_account_view(request, username):
    staff = get_object_or_404(Staff, username=username)
    user = User.objects.get(username=request.user.username)
    StaffUpdate_Account = StaffUpdateAccount(instance=staff)
    picture = '../' + staff.profile_pic.url
    if request.method=='POST':
        StaffUpdate_Account = StaffUpdateAccount(request.POST ,instance=staff)
        print(StaffUpdate_Account.errors)
        if StaffUpdate_Account.is_valid():
            print('valid')
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.save()
            staff = StaffUpdate_Account.save()
            staff.password = request.POST['password']
            staff.save()
            return redirect('../login')
    mydict = {'userForm':StaffUpdate_Account, 'picture':picture}
    return render(request,'profile/edit_customer_account.html', mydict)

# Phan cua Ngo Duc Vu - 20520950
@login_required(login_url='/login')
def nhapbienso_phieuthu(request, username):
    enquiry= NhapBienSoThu()
    staff = Staff.objects.get(username=username)
    picture = '../' + staff.profile_pic.url
    if request.method=='POST':
        enquiry= NhapBienSoThu(request.POST)
        if enquiry.is_valid():
            print('enquiry is valid')
            print(request.POST['bienso'])
            xe_x=Xe.objects.get(maxe=request.POST['bienso']) 
            return redirect(f'../{username}/nhap_phieuthu/{xe_x.maxe}')
    context= {'enquiry':enquiry, 'customer': staff, 'picture': picture}        
    return render(request,'phieuthutien/nhapbienso_phieuthu.html',context)

@login_required(login_url='/login')
def xacnhan_phieuthu(request,maxe, username):
    nhapsotienthu=NhapSoTienThu()
    staff = Staff.objects.get(username=username)
    picture = '../' + staff.profile_pic.url
    xe_x=Xe.objects.get(maxe=maxe)
    khach_x=KhachHang.objects.get(makhachhang=xe_x.makhachhang_id) 
    list_phieusua=PhieuSuaChua.objects.all().filter(maxe_id=xe_x.maxe)
    xe_x.save()
    context= {'nhapsotienthu':nhapsotienthu,'xe_x': xe_x,'khach_x':khach_x, 
                "customer": staff, "picture":picture, "data":list_phieusua} 
    if request.method=='POST':
        nhapsotienthu=NhapSoTienThu(request.POST)  
        if nhapsotienthu.is_valid():
            print('enquiry is valid')
            tienthu=nhapsotienthu.cleaned_data['sotienthu']
            if tienthu<xe_x.tienno:
                print('chua hoan thanh')
                return render(request,'phieuthutien/nhapsotienthu.html',context)   
            else: 
                phieuthutien_x=PhieuThuTien.objects.create(maxe_id=xe_x.maxe,sotienthu=tienthu)
                xe_x.tienno=0
                xe_x.save()
                print('da luu vao database')
                for i in list_phieusua:
                    i.tinhtrangthutien=1
                    i.save()
                print('da luu vao database')
    return render(request,'phieuthutien/nhapsotienthu.html',context)       

@login_required(login_url="/login")
def view_phieuthu(request,maphieuthutien):
    phieuthu=PhieuThuTien.objects.get(maphieuthutien=maphieuthutien)
    xe_x=Xe.objects.get(maxe=phieuthu.maxe)
    context={'xe_x':xe_x,'phieuthu':phieuthu}
    return render(request,'phieuthutien/view_phieuthu.html',context)       

@login_required(login_url="/login")
def nhapbiensosua(request,username):
    enquiry= NhapBienSoSua()
    staff = Staff.objects.get(username=username)
    picture = '../' + staff.profile_pic.url
    if request.method=='POST':
        enquiry=NhapBienSoSua(request.POST)
        print(request.POST['bienso'])
        xe_x=Xe.objects.get(bienso=request.POST['bienso'])
        phieusua_x=PhieuSuaChua.objects.create(maxe_id=xe_x.maxe,tongthanhtien=0)
        phieusua_x.save()
        return redirect(f'../{username}/view_phieusua/{phieusua_x.maphieusuachua}')
    return render(request,'phieusuachua/nhapbiensosua.html', {'enquiry':enquiry, 'customer': staff, 'picture':picture}, ) 

@login_required(login_url="/login")
def view_phieusua(request ,maphieusuachua, username):
    phieusua=PhieuSuaChua.objects.get(maphieusuachua=maphieusuachua)
    xe_x=Xe.objects.get(maxe=phieusua.maxe_id)
    data=CT_PhieuSuaChua.objects.all().filter(maphieusuachua=maphieusuachua)
    staff = Staff.objects.get(username=username)
    picture = '../' + staff.profile_pic.url
    enquiry=NhapCTSuaChua()
    context= {'phieusua':phieusua,'xe_x':xe_x,'data':data,'enquiry':enquiry, "customer":staff, "picture":picture}
    if request.method=='POST':
        print('request method la POST')
        enquiry=NhapCTSuaChua(request.POST)
        if enquiry.is_valid():
            print('enquiry is valid')
            tiencong_x=TienCong.objects.get(loaitiencong=enquiry.cleaned_data['loaitiencong'])
            tongtiencong=tiencong_x.tiencong*enquiry.cleaned_data['solan']
            phieusua_x=CT_PhieuSuaChua.objects.create(maphieusuachua_id=maphieusuachua,
            matiencong_id=tiencong_x.matiencong,tiencong=tongtiencong,
            solan=enquiry.cleaned_data['solan'], noidung=enquiry.cleaned_data['noidung'],tongtien=tongtiencong)
            tongthanhtien_x=phieusua.tongthanhtien+tongtiencong
            phieusua.tongthanhtien=tongthanhtien_x
            phieusua.save()
            #Cap nhat tien no
            xe_x=Xe.objects.get(maxe=phieusua.maxe_id)
            tienno_xe=xe_x.tienno+tongtiencong
            xe_x.tienno=tienno_xe
            xe_x.save()
            return render(request,'phieusuachua/view_phieusua.html',context) 
    return render(request,'phieusuachua/view_phieusua.html',context) 


@login_required(login_url="/login")
def view_ctphieusuachua(request,mact_phieusuachua, username):
    ct_phieusua=CT_PhieuSuaChua.objects.get(mact_phieusuachua=mact_phieusuachua)  
    data=CT_VatTuPhuTung.objects.all().filter(mact_phieusuachua=mact_phieusuachua)
    nhap_ctvtpt=NhapCT_VatTuPhuTung
    staff = Staff.objects.get(username=username)
    picture = '../' + staff.profile_pic.url
    context={'ct_phieusua':ct_phieusua,'nhap_ctvtpt':nhap_ctvtpt,'data':data,"customer":staff, "picture":picture}
    # context={'nhap_ctvtpt':nhap_ctvtpt}
    if request.method=='POST':
        print('request method is POST')
        nhap_ctvtpt=NhapCT_VatTuPhuTung(request.POST)
        if nhap_ctvtpt.is_valid():  
                print('phieu nhap is valid')
                tien1_ctvattu=nhap_ctvtpt.cleaned_data['dongia']*nhap_ctvtpt.cleaned_data['soluong']
                print(nhap_ctvtpt.cleaned_data['dongia'],'...',nhap_ctvtpt.cleaned_data['soluong'])
                vattu_x=VatTuPhuTung.objects.get(tenvattuphutung=nhap_ctvtpt.cleaned_data['tenvattuphutung'])
                CT_VatTuPhuTung.objects.create(mact_phieusuachua_id=mact_phieusuachua,
                mavattuphutung_id=vattu_x.mavattuphutung, soluong=nhap_ctvtpt.cleaned_data['soluong'],
                dongia=nhap_ctvtpt.cleaned_data['dongia'], tongthanhtien=tien1_ctvattu)
                tong_tatcavattu=tien1_ctvattu+ct_phieusua.tongtienvattu
                ct_phieusua.tongtienvattu=tong_tatcavattu
                ct_phieusua.tongtien=tong_tatcavattu+ct_phieusua.tiencong
                ct_phieusua.save()
                phieusua_x=PhieuSuaChua.objects.get(maphieusuachua=ct_phieusua.maphieusuachua_id)
                tong_phieusua=phieusua_x.tongthanhtien + tien1_ctvattu
                phieusua_x.tongthanhtien=tong_phieusua
                phieusua_x.save()
                #cap nhat tien no xe
                xe_x=Xe.objects.get(maxe=phieusua_x.maxe_id)
                tienno_xe=xe_x.tienno+tien1_ctvattu
                xe_x.tienno=tienno_xe
                xe_x.save()
                # capnhattienno(phieusua_x.maphieusuachua,tong_phieusua)                         
    return render(request,'phieusuachua/view_ctphieusua.html',context)

@login_required(login_url="/login")
def delete_ctphieusua(request,mact_phieusuachua,username):
    ctphieusua=CT_PhieuSuaChua.objects.get(mact_phieusuachua=mact_phieusuachua)
    phieusua_x=PhieuSuaChua.objects.get(maphieusuachua=ctphieusua.maphieusuachua_id)
    print(phieusua_x.tongthanhtien,'-',ctphieusua.tongtien)
    tongthanhtien_x=phieusua_x.tongthanhtien-ctphieusua.tongtien
    phieusua_x.tongthanhtien=tongthanhtien_x
    print(phieusua_x.tongthanhtien)
    #cap nhat tien no xe
    xe_x=Xe.objects.get(maxe=phieusua_x.maxe_id)
    tienno_xe=xe_x.tienno-ctphieusua.tongtien
    xe_x.tienno=tienno_xe
    xe_x.save()
    phieusua_x.save()
    ctphieusua.delete()
    maphieusuachua_x=int(phieusua_x.maphieusuachua)
    return redirect(f'../../{username}/view_phieusua/{phieusua_x.maphieusuachua}')

@login_required(login_url="/login")
def delete_chitietvattu(request,mact_vattuphutung,mact_phieusuachua,maphieusuachua,username):
    ctvt=CT_VatTuPhuTung.objects.get(mact_vattuphutung=mact_vattuphutung)
    ctphieusua=CT_PhieuSuaChua.objects.get(mact_phieusuachua=mact_phieusuachua)
    phieusua_x=PhieuSuaChua.objects.get(maphieusuachua=maphieusuachua)
    tien_1vattu=ctvt.soluong*ctvt.dongia
    tongtien=ctphieusua.tongtien-tien_1vattu
    tongtienvattu_x=ctphieusua.tongtienvattu-tien_1vattu
    ctphieusua.tongtienvattu=tongtienvattu_x
    ctphieusua.tongtien=tongtien
    tongthanhtien_x=phieusua_x.tongthanhtien-tien_1vattu
    phieusua_x.tongthanhtien=tongthanhtien_x
    #cap nhat tien no xe
    xe_x=Xe.objects.get(maxe=phieusua_x.maxe_id)
    tienno_xe=xe_x.tienno-tien_1vattu
    xe_x.tienno=tienno_xe
    xe_x.save()
    ctphieusua.save()
    phieusua_x.save()
    ctvt.delete()
    return redirect(f'/../../{username}/view_ctphieusua/{ctphieusua.mact_phieusuachua}')
