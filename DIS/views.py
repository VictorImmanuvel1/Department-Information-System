from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile,Education,student,oe,ap,article,seminar,sem1,sem2,sem3,sem4,sem5,event
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from .forms import registerform,sem1form,sem2form,sem3form,sem4form,sem5form,eventform,UserRegisterForm,ProfileUpdateForm,UserUpdateForm,EducationUpdateForm,oeForm,apForm,articleForm,seminarForm
from .filters import studentFilter

# Create your views here.

@unauthenticated_user
def log(request):                                   #login page which redirects admin and staff to the respective pages
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('adminHome')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('log')
    context = {}
    return render(request,'login.html')

def logoutUser(request):
	logout(request)
	return redirect('log')

@login_required(login_url='log')
@admin_only
def adhome(req):                                #admin homepage
    return render(req,'adminHome.html')

def student_reg(req):
    form = registerform()
    if req.method == 'POST':
        form = registerform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(req,'studentReg.html',context)

def student_detail(req):
    user=student.objects.all()
    myFilter = studentFilter(req.GET, queryset=user)
    user = myFilter.qs
    context={'user':user,'myFilter':myFilter}
    return render(req, 'liststudent.html', context)

def delete(req,pk):
    user = student.objects.get(id=pk)
    user2 = Profile.objects.get(id=pk)
    if req.method == "POST":
        user.delete()
        return redirect('/')
    context = {'item': user,'item2':user2}
    return render(req,'delete.html',context)

def stud_info(req,pk):
    user=student.objects.get(id=pk)
    mark=sem1.objects.get(sid=pk)
    mark1 = sem2.objects.get(sid=pk)
    mark2 = sem3.objects.get(sid=pk)
    mark3 = sem4.objects.get(sid=pk)
    mark4 = sem5.objects.get(sid=pk)

    context = {'user': user,'mark':mark,'mark1':mark1,'mark1':mark1,'mark2':mark2,'mark3':mark3,'mark4':mark4}
    return render(req, 'studentDetails.html', context)

def update(req,pk):
    user = student.objects.get(id=pk)
    form = registerform(instance=user)
    if req.method=='POST':
        form=registerform(req.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(req, 'updatepro.html', context)

def updatesem1(req,pk):
    mark = sem1.objects.get(sid=pk)
    form1 = sem1form(instance=mark)
    if req.method == 'POST':
        form1 = sem1form(req.POST,instance=mark)
        if form1.is_valid():
            form1.save()
            return redirect('/')

    context = {'form1': form1}
    return render(req, 'updatesem1.html',context)

def updatesem2(req,pk):
    mark1 = sem2.objects.get(sid=pk)
    form2 = sem2form(instance=mark1)
    if req.method == 'POST':
        form2 = sem2form(req.POST,instance=mark1)
        if form2.is_valid():
            form2.save()
            return redirect('/')

    context = {'form2': form2}
    return render(req, 'updatesem2.html',context)

def updatesem3(req,pk):
    mark2 = sem3.objects.get(sid=pk)
    form3 = sem3form(instance=mark2)
    if req.method == 'POST':
        form3 = sem3form(req.POST,instance=mark2)
        if form3.is_valid():
            form3.save()
            return redirect('/')

    context = {'form3': form3}
    return render(req, 'updatesem3.html',context)

def updatesem4(req,pk):
    mark3 = sem4.objects.get(sid=pk)
    form4 = sem4form(instance=mark3)
    if req.method == 'POST':
        form4 = sem4form(req.POST,instance=mark3)
        if form4.is_valid():
            form4.save()
            return redirect('/')

    context = {'form4': form4}
    return render(req, 'updatesem4.html',context)

def updatesem5(req,pk):
    mark4 = sem5.objects.get(sid=pk)
    form5 = sem5form(instance=mark4)
    if req.method == 'POST':
        form5 = sem5form(req.POST,instance=mark4)
        if form5.is_valid():
            form5.save()
            return redirect('/')

    context = {'form5': form5}
    return render(req, 'updatesem5.html',context)

def eventhome(req):
    return render(req,'eventHome.html')

def event_reg(req):
    form=eventform()
    if req.method=='POST':
        form=eventform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('eventhome')
    context={'form':form}
    return render(req,'eventrecord.html',context)

def event_view(req):
    eve=event.objects.all()
    context={'eve':eve}
    return render(req,'eventtable.html',context)

def staffreg(req):                              #staff registration
    form = UserRegisterForm()
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='staff')
            user.groups.add(group)

            messages.success(req, 'Account was created for ' + username)

            return redirect('log')

    context = {'form': form}
    return render(req,'staffReg.html',context)

@login_required(login_url='log')
@allowed_users(allowed_roles=['staff'])
def sthome(req):                                #staff homepage
    return render(req,'staffHome.html')

def staffview(req):
    user=Profile.objects.all()
    context={'user':user}
    return render(req,'stafflist.html',context)

def view(req):
    return render(req,'staffView.html')

def indview(req,pk):
    user=Profile.objects.get(id=pk)
    ed=Education.objects.get(id=pk)
    other=oe.objects.get(id=pk)
    aca=ap.objects.get(id=pk)
    art=article.objects.get(id=pk)
    semi=seminar.objects.get(id=pk)
    context={'user':user,'ed':ed,'other':other,'aca':aca,'art':art,'semi':semi}
    return render(req,'staff.html',context)


def updatestaff(req):
    if req.method=='POST':
        u_form=UserUpdateForm(req.POST,instance=req.user)
        p_form=ProfileUpdateForm(req.POST,instance=req.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('staffview')
    else:
        u_form=UserUpdateForm(instance=req.user)
        p_form = ProfileUpdateForm(instance=req.user.profile)

    context={'u_form':u_form,'p_form':p_form}
    return render(req,'staffUpdate.html',context)

def educationupdate(req):
    if req.method == 'POST':
        form = EducationUpdateForm(req.POST, instance=req.user.education)
        if form.is_valid():
            form.save()
            return redirect('staffview')
    else:
        form=EducationUpdateForm(instance=req.user.education)
    context={'form':form}
    return render(req,'educationupdate.html',context)

def oeupdate(req):
    if req.method == 'POST':
        form = oeForm(req.POST, instance=req.user.oe)
        if form.is_valid():
            form.save()
            return redirect('staffview')
    else:
        form = oeForm(instance=req.user.oe)
    context = {'form': form}
    return render(req, 'oeupdate.html', context)

def apupdate(req):
    if req.method == 'POST':
        form =apForm(req.POST, instance=req.user.ap)
        if form.is_valid():
            form.save()
            return redirect('staffview')
    else:
        form = apForm(instance=req.user.ap)
    context = {'form': form}
    return render(req, 'apupdate.html', context)

def articleupdate(req):
    if req.method == 'POST':
        form = articleForm(req.POST, instance=req.user.article)
        if form.is_valid():
            form.save()
            return redirect('staffview')
    else:
        form = articleForm(instance=req.user.article)
    context = {'form': form}
    return render(req, 'articleupdate.html', context)

def seminarupdate(req):
    if req.method == 'POST':
        s_form = seminarForm(req.POST, instance=req.user.seminar)
        if s_form.is_valid():
            s_form.save()
            return redirect('staffview')
    else:
        s_form = seminarForm(instance=req.user.seminar)
    context = {'s_form': s_form}
    return render(req, 'seminarupdate.html', context)


def passwordreset(req):
    return render(req,'passreset.html')

def resetdone(req):
    return render(req,'passresetdone.html')