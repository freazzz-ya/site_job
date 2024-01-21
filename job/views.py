from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ContestForm
from users.models import Worker


def job_view(request):
    return render(request, 'main/index.html')


def neiro_view(request):
    return render(request, 'main/press-single.html')


@login_required
def finance_view(request):
    worker = Worker.objects.get(id=1)
    context = {
        'worker': worker,
    }
    return render(request, 'main/single.html', context)

