from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import ListView
from PIL import Image

from users.models import Special, Worker

from .crypto.api import return_api
from .forms import (Earning_schemeForm, Job_Reg_Form, JobForm,
                    Maling_model_form, NetworkForm, NeuralNetworkForm,
                    Other_Source_Form, Other_Source_Reg_Form, SpecialForm,
                    Сontacts_model_form, Expenses_model_form)
from .models import (Crypto_model, Earning_scheme, Job, Job_Payment,
                     Network_Payment, Neural_network, Other_Source,
                     Other_Source_model, Expenses_model)


USERS_FOR_USIBILLITY = 100


def categogy_count():
    """Подсчет категории"""
    count_networks = Neural_network.objects.count()
    count_worker = Worker.objects.count() + USERS_FOR_USIBILLITY
    count_scheme = Earning_scheme.objects.count()
    count_job = Job.objects.count()
    other_source_model = Other_Source_model.objects.count()
    forms = [
        count_networks, count_worker, count_scheme,
        count_job, other_source_model,
    ]
    return forms


def job_view(request):
    if request.method == 'POST':
        form_contacts = Сontacts_model_form(request.POST, request.FILES)
        form_maling = Maling_model_form(request.POST, request.FILES)
        if form_maling.is_valid():
            form_maling = form_maling.save()
            return redirect(request.META.get('HTTP_REFERER'))
        if form_contacts.is_valid():
            form_contacts = form_contacts.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form_contacts = Сontacts_model_form()
        form_maling = Maling_model_form()
    count_networks = Neural_network.objects.count()
    #  Добавим видимость посещаемости сайта
    count_worker = Worker.objects.count() + USERS_FOR_USIBILLITY
    context = {
        'form_maling': form_maling,
        'form_contacts': form_contacts,
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
    else:
        form = NeuralNetworkForm()
    context = {
        'networks': networks,
        'form': form,
    }
    return render(request, 'main/press-single.html', context)


@login_required
def finance_view(request):
    stable_expenses = sum(Expenses_model.objects.filter(
        author_id=request.user.id, type_expenses='Постоянные расходы',).
                          values_list('price', flat=True)
    )
    variable_expenses = sum(Expenses_model.objects.filter(
        author_id=request.user.id, type_expenses='Переменные расходы',).
                            values_list('price', flat=True)
    )
    unexpected_expenses = sum(Expenses_model.objects.filter(
        author_id=request.user.id, type_expenses='Неожиданные расходы',).
                              values_list('price', flat=True)
    )
    planned_expenses = sum(Expenses_model.objects.filter(
        author_id=request.user.id,
        type_expenses='Планируемые заранее расходы',).
                           values_list('price', flat=True)
    )
    amount_expenses = sum([
        stable_expenses, variable_expenses,
        unexpected_expenses, planned_expenses,]
    )
    monthly_income = Expenses_model.objects.filter(
        author_id=request.user.id,
        date__month=timezone.now().month,
        date__year=timezone.now().year
    ).values('type_expenses').annotate(
        total_price=Sum('price')).order_by('type_expenses')
    amount_expenses_month = sum(Expenses_model.objects.filter(
        author_id=request.user.id,
        date__month=timezone.now().month,
        date__year=timezone.now().year).values_list(
            'price', flat=True))
    date_now = timezone.now().strftime('%B')
    income_job = sum(Job_Payment.objects.filter(
        worker_id=request.user.id,
        date__month=timezone.now().month,
        date__year=timezone.now().year).values_list(
            'payment_in_money', flat=True)
        )
    income_other_source = sum(Other_Source.objects.filter(
        worker_id=request.user.id,
        date__month=timezone.now().month,
        date__year=timezone.now().year).values_list(
            'payment_in_money', flat=True))
    income_network = sum(Network_Payment.objects.filter(
        worker_id=request.user.id,
        date__month=timezone.now().month,
        date__year=timezone.now().year).values_list(
            'payment_in_money', flat=True)
        )
    income_sum_month = sum((income_network, income_other_source, income_job))
    forms = categogy_count()
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
        'forms': forms,
        'day_amount': day_amount,
        'total_amount': total_amount,
        'sum_job': sum_job,
        'sum_network': sum_network,
        'sum_other': sum_other,
        'user': user,
        'form': form,
        'form1': form1,
        'form2': form2,
        'stable_expenses': stable_expenses,
        'variable_expenses': variable_expenses,
        'unexpected_expenses': unexpected_expenses,
        'planned_expenses': planned_expenses,
        'amount_expenses': amount_expenses,
        'monthly_income': monthly_income,
        'amount_expenses_month': amount_expenses_month,
        'date_now': date_now,
        'income_job': income_job,
        'income_other_source': income_other_source,
        'income_network': income_network,
        'income_sum_month': income_sum_month,
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
            'date', 'duration', 'worker',
            'comment',
            ).reverse()
    job = Job_Payment.objects.filter(
        worker__id=request.user.id
        ).values_list(
            'payment_in_money', 'busyness',
            'date', 'duration',
            'comment',
            ).reverse()
    network = Network_Payment.objects.filter(
        worker__id=request.user.id
        ).values_list(
            'payment_in_money', 'busyness',
            'date', 'duration',
            'comment',
            ).reverse()
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


def earning_scheme(request):
    """Схема заработка"""
    scheme = Earning_scheme.objects.all()
    if request.method == 'POST':
        form = Earning_schemeForm(request.POST, request.FILES)
        if form.is_valid():
            sheme_form = form.save(commit=False)
            sheme_form.worker = request.user
            sheme_form.save()
            return redirect('/job/scheme/')
    else:
        form = Earning_schemeForm()
    forms = categogy_count()
    context = {
        'scheme': scheme,
        'form': form,
        'forms': forms,
    }
    return render(request, 'main/syst.html', context)


class CryptoListView(ListView):
    model = Crypto_model
    template_name = 'main/crypto.html'
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        forms = categogy_count()
        context['forms'] = forms
        api_values, shares_values = return_api()
        context['api_values'] = api_values
        context['shares_values'] = shares_values
        return context


@login_required
def finance_calculation_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        form1 = NetworkForm(request.POST, request.FILES)
        form2 = Other_Source_Form(request.POST, request.FILES)
        form3 = Expenses_model_form(request.POST, request.FILES)
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
        if form3.is_valid():
            other_payment = form3.save(commit=False)
            other_payment.author = request.user
            other_payment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = JobForm()
        form1 = NetworkForm()
        form2 = Other_Source_Form()
        form3 = Expenses_model_form()
    context = {
        'form': form,
        'form1': form1,
        'form2': form2,
        'form3': form3,
    }
    return render(request, 'main/finance_calculation.html', context)


@login_required
def finance_list_expenses(request):
    expenses = Expenses_model.objects.filter(
        author_id=request.user.id). values(
            'price', 'comment', 'type_expenses',
            'variety', 'date'
        )
    expenses_amount = sum(Expenses_model.objects.filter(
        author_id=request.user.id).values_list('price', flat=True))
    context = {
               'expenses': expenses,
               'expenses_amount': expenses_amount,
    }
    return render(request, 'main/expenses_list.html', context)
