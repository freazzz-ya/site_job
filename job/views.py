from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image

from users.models import Worker
from .models import Neural_network
from .forms import NeuralNetworkForm, JobForm, NetworkForm, Other_Source_Form


def job_view(request):
    count_networks = Neural_network.objects.count()
    #  Добавим видимость посещаемости сайта
    count_worker = Worker.objects.count() + 100
    context = {
        'count_networks': count_networks,
        'count_worker': count_worker,
    }
    return render(request, 'main/index.html', context)


def neiro_view(request):
    networks = Neural_network.objects.all()
    if request.method == 'POST':
        form = NeuralNetworkForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  # Сначала получаем экземпляр без сохранения в БД
            if instance.image:  # Проверяем, загружено ли изображение
                img = Image.open(instance.image)
                img.thumbnail((300, 200))  # Изменяем размер до 300x300
                img.save(instance.image.path)  # Перезаписываем изображение
            instance.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = NeuralNetworkForm()
    context = {
        'networks': networks,
        'form': form,
    }
    return render(request, 'main/press-single.html', context)


@login_required
def finance_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        form1 = NetworkForm(request.POST, request.FILES)
        form2 = Other_Source_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = JobForm()
        form1 = NetworkForm()
        form2 = Other_Source_Form()
    user = Worker.objects.get(id=request.user.id)
    context = {
        'user': user,
        'form': form,
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'main/single.html', context)

