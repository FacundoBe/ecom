from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm


@login_required
def dashboard(request):
    items=Item.objects.filter(created_by=request.user)
    return render(request,'dashboard.html',{'items':items} )


@login_required
def new_conversation(request, item_pk):
    item=get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user: #en caso que el item pertenezca al usuario loggeado
        return redirect('index')
    
    #Check for previous conversations between user and item owner
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id]) 
                                                                                                        
    if conversations:
        return redirect('detail_conversation',pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid:
             conversation = Conversation.objects.create(item=item)
             conversation.members.add(request.user)
             conversation.members.add(item.created_by)
             conversation.save()

             conversation_message = form.save(commit=False)
             conversation_message.conversation=conversation
             conversation_message.created_by=request.user
             conversation_message.save()

             return redirect('detail',pk=item_pk)
    else:
        form = ConversationMessageForm()
    return render(request,'new_conversation.html',{'form':form})


@login_required
def detail_conversation(request, pk):
    # el filtro grantiza que no se pueda accededr a conversaciones ajenas usando, solo a las que tienen al usuario logeado 
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid:
             conversation_message = form.save(commit=False)
             conversation_message.conversation=conversation
             conversation_message.created_by=request.user
             conversation_message.save()

             conversation.save() # LA grabo para que se actualize la fecha de modificacion con al de este mensaje

             return redirect( 'detail_conversation', pk=pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'detail_conversation.html',{'conversation':conversation,'form':form})  



@login_required
def inbox(request):

    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'inbox.html',{'conversations':conversations})  

