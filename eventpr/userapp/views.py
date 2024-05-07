from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                return redirect('register/')
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                return redirect('/')
        else:
            return redirect('register/')
    return render(request,'reg.html')