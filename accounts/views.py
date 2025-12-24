from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    except Exception as e:
        profile =  None
        print(f"Error getting profile:{e}")
    context={
        'profile':profile
    }
    return render(request, 'accounts/profile.html', context )

@staff_member_required
def admin_dashboard(request):
    # if not request.user.is_staff:
    #     return redirect('accounts:login')
    total_users = User.objects.count()
    recent_users = User.objects.order_by('-date_joined')[:5]
    
    context = {
        'total_users': total_users,
        'recent_users': recent_users,
    }
    return render(request, 'accounts/admin_dashboard.html', context)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Save additional profile information
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.phone_number = form.cleaned_data.get('phone_number')
            profile.address = form.cleaned_data.get('address')
            profile.city = form.cleaned_data.get('city')
            profile.state = form.cleaned_data.get('state')
            profile.zip_code = form.cleaned_data.get('zip_code')
            profile.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back {user.username}!')
            return redirect('accounts:home')  # Replace with your home page URL
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
