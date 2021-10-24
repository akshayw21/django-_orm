from ormapp.form import EmpForm,AccountForm,EmpqualificationForm,UserForm1,UserForm2
from django.shortcuts import render,redirect
from .models import Empqualification, Teacher,Emp,Account
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_student(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        college=request.POST.get('college')
        t=Teacher()
        t.name=name
        t.email=email
        t.contact=contact
        t.college=college
        t.save()

        return render(request,'home.html')
    else:
        return render(request,'addstudent.html')

def add_emp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')

    else:
        d={'form':EmpForm}
        return render(request,'addemp.html',d)


def add_account(request):
    if request.method=='POST':
        f=AccountForm(request.POST)
        f.save()

        return redirect('/')
    else:
        d={'form':AccountForm}
        return render(request,'addaccount.html',d)


def emp_list(request):
    el=Emp.objects.all()
    context={'elist':el}
    return render(request,'emplist.html',context)

def student_list(request):
    sl=Teacher.objects.all()
    student={'slist':sl}
    return render(request,'studentlist.html',student)

def account_list(request):
    al=Account.objects.all()
    account={'acclist':al}
    return render(request,'accountlist.html',account)

def delete_Emp1(request):
    e_mail=request.GET.get('email')
    e1=Emp.objects.get(email=e_mail)
    e1.delete()
    return redirect('/emplist')

def edit_Emp(request,email):
    e1=Emp.objects.get(email=email)
    
    if request.method=='POST':
        e=EmpForm(request.POST,instance=e1)
        e.save()
        return redirect('/emplist')
    else:
        f=EmpForm(instance=e1)
        context={'form':f}
        return render(request,'form.html',context)

def delete_Emp2(request,email):
    e1=Emp.objects.get(email=email)
    e1.delete()
    return redirect('/emplist')

def delete_Acc(request):
    id=request.GET.get('id')
    i1=Account.objects.get(id=id)
    i1.delete()
    return redirect('/accountlist')

#def edit_Acc(request,id):
    #a1=Account.objects.get(id=id)

    #if request.method=='POST':


def delete_Acc2(request,email):
    i1=Account.objects.get(email=email)
    i1.delete()
    return redirect('/accountlist')



def add_qualif(request):
    if request.method=='POST':
        f=EmpqualificationForm(request.POST)  
        f.save()
        return redirect('/')
    else:
        d={'form':EmpqualificationForm}
        return render(request,'form.html',d)


def add_user1(request):
    if request.method=='POST':
        f=UserForm1(request.POST)
        f.save()
        return redirect('/')
    else:
        d={'form':UserForm1}
        return render(request,'form.html',d)


def add_user2(request):
    if request.method=='POST':
        f=UserForm2(request.POST)
        f.save()
        return redirect('/')
    else:
        d={'form':UserForm2}
        return render(request,'form.html',d)

from django.contrib.auth.forms import UserCreationForm
from .form import UserForm3

def add_user3(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')

    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'form.html',context)


def add_user4(request):
    if request.method=='POST':
        f=UserForm3(request.POST)
        f.save()
        return redirect('/')

    else:
        f=UserForm3
        context={'form':f}
        return render(request,'form.html',context)

from .form import UserInfoForm,UserInfoForm2
def add_user5(request):
    if request.method=='POST':
        f=UserInfoForm(request.POST)
        f.save()
        return redirect('/')

    else:
        f=UserInfoForm
        context={'form':f}
        return render(request,'form.html',context)

def add_user6(request):
    if request.method=='POST':
        f=UserInfoForm2(request.POST)
        f.save()
        return redirect('/')

    else:
        f=UserInfoForm2
        context={'form':f}
        return render(request,'form.html',context)

from .form import SingerForm,SongsForm,Songs,Singer

def add_singer(request):
    if request.method=='POST':
        f=SingerForm(request.POST)
        f.save()
        return redirect('/')

    else:
        d={'form':SingerForm}
        return render(request,'form.html',d)

def add_songs(request):
    if request.method=='POST':
        f=SongsForm(request.POST)
        f.save()
        return redirect('/')

    else:
        d={'form':SongsForm}
        return render(request,'form.html',d)


def singer_list(request):
    sgl=Singer.objects.all()
    context={'singerlist':sgl}
    return render(request,'singerlist.html',context)


def songs_list(request):
    sol=Songs.objects.all()
    context={'songslist':sol}
    return render(request,'songslist.html',context)



