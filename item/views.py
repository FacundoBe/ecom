from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import Item
from .forms import NewItemForm


def detail(request,pk):
    item= get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    #el exclude es para que no incluya el item actual, ademas guardo solo los primeros 3 items
    return render(request, 'detail.html', {'item':item,'related_items':related_items})

@login_required
def new(request):
    form=NewItemForm()
    render (request,'new.html',{'form':form,'title':'New Item'})