from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .forms import UserForm
from .models import Details
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        print(form.is_valid())
        # if the username minlengh will be 5 and max length will be 20 then only the form is valid
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            userDetails = User.objects.create_user(username=username, password=password, email=email)
            userDetails.is_staff = False
            userDetails.is_superuser = False
            userDetails.first_name = firstName
            userDetails.last_name = lastName
            userDetails.save()
            myprofile = request.FILES.get('image')
            myfile = request.FILES.get('file')
            user = User.objects.get(username=username)
            user_id = user.pk
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile) # this will save the files in the system in the media folder
            uploaded_file_url = fs.url(filename)
            my_file = fs.save(myprofile.name, myprofile)
            uploaded_file_url1 = fs.url(filename)
            personal_data = Details(user_id=user_id, image=myprofile, file=myfile)  # this will save files in the models that we specified
            personal_data.save()
            return render(request, 'welcome.html', {'url': uploaded_file_url})
    else:
        form = UserForm()
        return render(request, 'welcome.html', {'form': form})


@csrf_protect
def registerform(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        userDetails = User.objects.create_user(username=username, password=password, email=email)
        userDetails.is_staff = False
        userDetails.is_superuser = False
        userDetails.first_name = firstName
        userDetails.last_name = lastName
        userDetails.save()
        myprofile = request.FILES.get('profileImage')
        myfile = request.FILES.get('uploadFile')
        fs = FileSystemStorage()
        fileName = fs.save(myprofile.name, myprofile)
        imageName = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(fileName)
        uploaded_file_url1 = fs.url(imageName)
        print(username)
        print(myprofile)
        print(myfile)
        user = User.objects.get(username=username)
        user_id = user.pk
        personal_data = Details(user_id=user_id, image=myprofile, file=myfile)
        personal_data.save()
        return render(request, 'register.html', {'url': uploaded_file_url})
    else:
        return render(request, 'register.html', {})
