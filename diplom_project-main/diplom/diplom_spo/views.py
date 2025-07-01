from django.shortcuts import render, get_object_or_404, redirect
from .models import Diplom
from .forms import DiplomForm
from django.urls.base import reverse


# def index(request):
#     return HttpResponse('Диплом ПОКАЖИ!!!!!')


def index(request):
    diploms = Diplom.objects.all()
    return render(request, 'diplom/diplom_list.html', {'diploms': diploms})


# def diplom_edit(request, pk):
#     diplom = get_object_or_404(Diplom, pk=pk)
#     if request.method == 'POST':
#         form = DiplomForm(request.POST, instance=diplom)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('diplom_spo:index'))
#     else:
#         form = DiplomForm(instance=diplom)
#     return render(request, 'includes/diplom_form.html', {'form': form})

def diplom_edit(request, pk):
    diplom = get_object_or_404(Diplom, pk=pk)
    if request.method == 'POST':
        form = DiplomForm(request.POST, instance=diplom)  
        if form.is_valid():
            form.save()  
            return redirect(reverse('diplom_spo:index'))  
        else:
            print(form.errors) 
    else:
        form = DiplomForm(instance=diplom)  
    return render(request, 'includes/diplom_form.html', {'form': form, 'diplom': diplom}) 


# def diplom_create(request):
#     if request.method == 'POST':
#         form = DiplomForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('diplom_spo:index'))
#     else:
#         form = DiplomForm()
#     return render(request, 'includes/diplom_form.html', {'form': form})

def diplom_create(request):
    if request.method == 'POST':
        form = DiplomForm(request.POST, request.FILES)  
        if form.is_valid():
            diplom = form.save()
            return redirect(reverse('diplom_spo:index'))
        else:
            print(form.errors)  
            return render(request, 'diplom/diplom_form.html', {'form': form}) 
    else:
        form = DiplomForm()
    return render(request, 'diplom/diplom_form.html', {'form': form})  


# def diplom_create(request):
#     form = DiplomForm(
#         request.POST or None,
#         files=request.FILES or None
#     )
#     if form.is_valid():
#         form.save()  # сохраняем паспорт в базу данных
#         return redirect(reverse('diplom:index'))  # перенаправляем на главную страницу
#     return render(request, 'diplom/diplom_create.html', {'form': form})
