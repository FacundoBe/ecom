from django.shortcuts import render
from item.models import  Category,Item
from .forms import SignupForm

def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    
    return render(request, 'index.html',{
                    'items':items, 
                    'categories':categories
    })


def contact(request):
    return render(request, 'contact.html',{})

def signup(request):
    form = SignupForm()
    if request.method=='POST':
        form = SignupForm(request.POST)
        
    return render(request,'signup.html',{'form':form})
    

    
