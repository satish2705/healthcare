from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from .forms import RegistrationForm
from .models import Activity


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, './register.html', {'form': form})
    
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, './signin.html', {'error': 'Invalid credentials'})
    return render(request, './signin.html')

@user_passes_test(lambda u: u.is_superuser)
def upload_data(request):
    # Code for uploading data goes here
    return render(request, './upload_data.html')

def cnn(request):
    # Code for training CNN goes here
    return render(request, './cnn.html')

def predict(request):
    # Code for making predictions goes here
    return render(request, './predict.html')

def medication(request):
    # Code for generating medication plan goes here
    return render(request, './medication.html')

def home(request):
    recent_activities = Activity.objects.order_by('-activity_time')[:10]  # Fetch the 10 most recent activities
    return render(request, './dashboard.html', {'recent_activities': recent_activities})

