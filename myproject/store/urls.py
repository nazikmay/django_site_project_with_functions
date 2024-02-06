from django.urls import path, include
from .views import goods_list, goods_create, goods_update, goods_detail, goods_delete, get_context_data


urlpatterns = [

    path('',get_context_data, name='goods_list'),
    path('<int:pk>', goods_detail, name='goods_detail'),
    path('create/', goods_create, name='goods_create'),
    path('<int:pk>/update/', goods_update, name='goods_update'),
    path('<int:pk>/delete/', goods_delete, name='goods_delete'),

]