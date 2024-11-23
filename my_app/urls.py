from django.urls import path
from . import views

urlpatterns = [
    path("myapp/", views.my_app, name="my_app"),
    path('', views.add_item, name='add_item'),
    path('item-list/', views.item_list, name='item_list'),
    path('update-item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),
]