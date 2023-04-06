from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import NewUserForm
from .models import Profile
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/myapp/product')    


    form = NewUserForm()
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request,'users/profile.html')


def create_profile(request):
    
    if request.method=="POST":
        contact = request.POST.get('contact')
        image = request.FILES['upload']
        user = request.user
        
        profile = Profile(img=image, user=user, phone=contact)
        profile.save()
        return redirect('/users/profile')
        
    
    return render(request,'users/create_profile.html')

def seller_profile(request,pk):
    seller = User.objects.get(pk=pk)
    context = {
        'seller':seller
    }
    return render(request,'users/seller_profile.html', context)