from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

from .utils import searchProfiles,paginateProfiles
from .models import Profile
from .forms import AppointmentForm, CustomUserCreationForm,ProfileForm,MessageForm,QualificationForm,RoleForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def loginUser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
             messages.error(request,'Username does not exit')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        
        else:
            messages.error(request,'Username or password is incorrect')

    return render(request,'users/login_register.html')

def logoutUser(request):
    messages.error(request,'User was logged out')
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    roleform = RoleForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        roleform = RoleForm(request.POST)
        role = request.POST['role']
        if form.is_valid() and roleform.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profile = Profile.objects.get(user = user)
            profile.role = role
            profile.save()
            roleform.save()
            messages.success(request,'User account was created')

            login(request,user)
            return redirect('edit-account')
        
        else:
            messages.error(request,'An error has occurred during registration')

    context={'page':page,'form':form,'roleform':roleform}
    return render(request,'users/login_register.html',context)
    
def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {"profiles":profiles,'search_query':search_query,'custom_range': custom_range}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    qualifications = profile.qualification_set.all()
    context = {'profile':profile,'qualifications':qualifications}
    return render(request,'users/user-profile.html',context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    blogs = profile.blog_set.all()
    qualifications = profile.qualification_set.all()
    bool_blogs = blogs.count()>0
    bool_qualifications = qualifications.count()>0
    context={'profile':profile,'blogs':blogs,'qualifications':qualifications,'bool_blogs':bool_blogs,'bool_qualifications':bool_qualifications}
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)

        if form.is_valid():
            form.save()
            return redirect('account')

    context={'form':form}
    return render(request,'users/profile_form.html',context)

@login_required(login_url='login')
def createQualification(request):
    profile = request.user.profile
    form = QualificationForm()
    
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.owner = profile
            qualification.save()
            messages.success(request, 'Qualification was added successfully!')
            return redirect('account')

    context={'form':form}
    return render(request,'users/qualification_form.html',context)

@login_required(login_url='login')
def updateQualification(request,pk):
    profile = request.user.profile
    qualification = profile.qualification_set.get(id=pk)
    form = QualificationForm(instance = qualification)

    if request.method == 'POST':
        form = QualificationForm(request.POST,instance = qualification)
        if form.is_valid():
            form.save()
            messages.success(request, 'Qualification was updated successfully!')
            return redirect('account')
    context={'form':form}
    return render(request,'users/qualification_form.html',context)

@login_required(login_url ='login')
def deleteQualification(request,pk):
    profile = request.user.profile
    qualification = profile.qualification_set.get(id=pk)
    
    if request.method == 'POST':
        qualification.delete()
        messages.success(request, 'Qualification was deleted successfully!')
        return redirect('account')

    context = {'object': qualification}
    return render(request,'delete_template.html',context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request,'users/inbox.html',context)

@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()

    context={'message':message}
    return render(request,'users/message.html',context)

def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request,'Your message was successfully sent!')
            return redirect('user-profile',pk=recipient.id)
    context = {'recipient': recipient, 'form': form}
    return render(request,'users/message_form.html',context)

@login_required(login_url='login')
def appointmentInbox(request):
    profile = request.user.profile
    appointmentRequests = profile.appointments.all()
    Count = appointmentRequests.count()
    context = {'appointmentRequests': appointmentRequests, 'Count': Count}
    return render(request,'users/appointmentInbox.html',context)

@login_required(login_url='login')
def viewAppointment(request,pk):
    profile = request.user.profile
    appointment = profile.appointments.get(id=pk)
    context={'appointment':appointment}
    return render(request,'users/appointment.html',context)


def createAppointment(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = AppointmentForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.sender = sender
            appointment.recipient = recipient

            if sender:
                appointment.name = sender.name
                appointment.email = sender.email
            appointment.save()

            messages.success(request,'Your Appointment is set successfully!')
            return redirect('user-profile',pk=recipient.id)
    context = {'recipient': recipient, 'form': form}
    return render(request,'users/appointment_form.html',context)

@login_required(login_url ='login')
def deleteAppointment(request,pk):
    profile = request.user.profile
    appointment = profile.appointments.get(id=pk)

    
    
    if request.method == 'POST':
        subject = 'Advika Appointment'
        ## SET MESSAGE
        message = appointment.subject

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
            fail_silently=False,
        )
        appointment.delete()
        messages.success(request, 'Appointment was deleted successfully!')
        return redirect('account')

    context = {'appointment': appointment}
    return render(request,'users/deleteAppointment.html',context)