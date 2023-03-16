from django.urls import path

from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard' ),
    path('new/<int:item_pk>', views.new_conversation, name='new_conversation' ),
    path('detail_conversation/<int:pk>', views.detail_conversation, name='detail_conversation' ),
      path('inbox/', views.inbox, name='inbox' ),                                                             
]
