from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required 
from .models import Item
from .forms import NewItemForm,EditItemForm


def detail(request,pk):
    item= get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    #el exclude es para que no incluya el item actual, ademas guardo solo los primeros 3 items
    return render(request, 'detail.html', {'item':item,'related_items':related_items})

@login_required
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by= request.user
            item.save()

            return redirect('detail', pk=item.id)
    else:
        form=NewItemForm()

    title="New Item"
    return render (request,'new.html',{'form':form,'title':title})


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'new.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard')