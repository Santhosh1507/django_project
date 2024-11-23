from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item

def my_app(request):
    return HttpResponse("Hello, world. You're at the polls index.") 


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to a page that displays the list of items
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list page after updating
    else:
        form = ItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list') 
    return render(request, 'confirm_delete.html', {'item': item})