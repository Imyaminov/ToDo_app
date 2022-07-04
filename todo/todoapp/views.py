from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request, ('Item has been added to list!'))
            context = {'all_items': all_items}
            return render(request, 'home.html', context)
    else:
        all_items = List.objects.all()
        return render(request, 'home.html', {'all_items': all_items})

def delete_item(request, pk):
    item = List.objects.get(id=pk)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect('home')

def cross_off(request, pk):
    item = List.objects.get(id=pk)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, pk):
    item = List.objects.get(id=pk)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, pk):
    if request.method == 'POST':
        item = List.objects.get(id=pk)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited!'))
            return redirect('home')
    else:
        item = List.objects.get(id=pk)
        return render(request, 'edit.html', {'item': item})



















