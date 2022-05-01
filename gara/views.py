from django.shortcuts import render
from . import forms

# Create your views here.
def tiep_nhan(request):
    form=forms.TiepNhanForm()
    
    mydict={'forms':form}

    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if forms.is_valid():
            print('save')
        return render(request,'hospital/admin_add_doctor.html',context=mydict)
    return render(request,'gara/add_request.html',{'enquiry':form})
