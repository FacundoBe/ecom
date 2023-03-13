from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models    import Item

@login_required
def dashboard(request):
    items=Item.objects.filter(created_by=request.user)
    return render(request,'dashboard.html',{'items':items} )

