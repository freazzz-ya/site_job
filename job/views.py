from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from PIL import Image

from users.models import Worker, Special
from .models import Neural_network, Other_Source, Network_Payment, Job_Payment
from .forms import (
    NeuralNetworkForm, JobForm, NetworkForm,
    Other_Source_Form, Job_Reg_Form, Other_Source_Reg_Form,
    SpecialForm,
    )

USERS_FOR_USIBILLITY = 100


def job_view(request):
    count_networks = Neural_network.objects.count()
    #  Добавим видимость посещаемости сайта
    count_worker = Worker.objects.count() + USERS_FOR_USIBILLITY
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
            # Сначала получаем экземпляр без сохранения в БД
            instance = form.save(commit=False)
            if instance.image:  # Проверяем, загружено ли изображение
                img = Image.open(instance.image)
                img.thumbnail((300, 200))  # Изменяем размер до 300x300
                img.save(instance.image.path)  # Перезаписываем изображение
            instance.save()
        return redirect('/job/finance/')
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
            job_payment = form.save(commit=False)
            job_payment.worker = request.user
            job_payment.save()
            return redirect(request.META.get('HTTP_REFERER'))
        if form1.is_valid():
            network_payment = form1.save(commit=False)
            network_payment.worker = request.user
            network_payment.save()
            return redirect(request.META.get('HTTP_REFERER'))
        if form2.is_valid():
            other_payment = form2.save(commit=False)
            other_payment.worker = request.user
            other_payment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = JobForm()
        form1 = NetworkForm()
        form2 = Other_Source_Form()
    user = Worker.objects.get(id=request.user.id)
    sum_other = sum(Other_Source.objects.filter(
        worker_id=request.user.id
        ).values_list('payment_in_money', flat=True))
    day_other = sum(Other_Source.objects.filter(
        worker_id=request.user.id
        ).values_list('duration', flat=True))
    sum_network = sum(Network_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('payment_in_money', flat=True))
    day_network = sum(Network_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('duration', flat=True))
    sum_job = sum(Job_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('payment_in_money', flat=True))
    day_job = sum(Job_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('duration', flat=True))
    day_amount = sum([day_other, day_network, day_job])
    total_amount = sum([sum_other, sum_network, sum_job])
    context = {
        'day_amount': day_amount,
        'total_amount': total_amount,
        'sum_job': sum_job,
        'sum_network': sum_network,
        'sum_other': sum_other,
        'user': user,
        'form': form,
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'main/single.html', context)


@login_required
def finance_add_work(request):
    """Добавление работы"""
    if request.method == 'POST':
        form3 = Job_Reg_Form(request.POST, request.FILES)
        form4 = Other_Source_Reg_Form(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
            return redirect('/job/finance/')
        if form4.is_valid():
            form4.save()
            return redirect('/job/finance/')
    else:
        form3 = Job_Reg_Form()
        form4 = Other_Source_Reg_Form()
    context = {
        'form3': form3,
        'form4': form4,
    }
    return render(request, 'main/single_add.html', context)


@login_required
def finance_other_add(request):
    """Добавление подработки"""
    if request.method == 'POST':
        form4 = Other_Source_Reg_Form(request.POST, request.FILES)
        if form4.is_valid():
            form4.save()
            return redirect('/job/finance/')
    else:
        form4 = Other_Source_Reg_Form()
    context = {
        'form4': form4,
    }
    return render(request, 'main/single_other_add.html', context)


@login_required
def finance_list(request):
    """Общая информация о финансах"""
    user = Worker.objects.get(id=request.user.id)
    sum_other = sum(Other_Source.objects.filter(
        worker_id=request.user.id
        ).values_list('payment_in_money', flat=True))
    sum_network = sum(Network_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('payment_in_money', flat=True))
    sum_job = sum(Job_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('payment_in_money', flat=True))
    total_amount = sum([sum_other, sum_network, sum_job])
    other_sources = Other_Source.objects.filter(
        worker__id=request.user.id
        ).values_list(
            'payment_in_money', 'busyness',
            'last_updated', 'duration', 'worker',
            ).reverse()[:5]
    job = Job_Payment.objects.filter(
        worker__id=request.user.id
        ).values_list(
            'payment_in_money', 'busyness',
            'last_updated', 'duration',
            ).reverse()[:5]
    network = Network_Payment.objects.filter(
        worker__id=request.user.id
        ).values_list(
            'payment_in_money', 'busyness',
            'last_updated', 'duration',
            ).reverse()[:5]
    day_other = sum(Other_Source.objects.filter(
        worker_id=request.user.id
        ).values_list('duration', flat=True))
    day_network = sum(Network_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('duration', flat=True))
    day_job = sum(Job_Payment.objects.filter(
        worker_id=request.user.id
        ).values_list('duration', flat=True))
    day_amount = sum([day_other, day_network, day_job])
    other_value = user.other_sources.all()
    network_value = user.network.all()
    job_value = user.job.all()
    context = {
        'day_job': day_job,
        'day_network': day_network,
        'day_other': day_other,
        'job_value': job_value,
        'network_value': network_value,
        'other_value': other_value,
        'day_amount': day_amount,
        'network': network,
        'job': job,
        'total_amount': total_amount,
        'sum_job': sum_job,
        'sum_network': sum_network,
        'sum_other': sum_other,
        'other_sources': other_sources,
        'user': user,
    }
    return render(request, 'main/single_list.html', context)


@login_required
def special(request):
    """Специальная вкладка"""
    special = Special.objects.all()
    if request.method == 'POST':
        form = SpecialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/job/finance/special/')
    else:
        form = SpecialForm()
    context = {
        'form': form,
        'special': special,
    }
    return render(request, 'main/special.html', context)
