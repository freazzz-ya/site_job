from django.shortcuts import render

# Create your views here.


def job_view(request):
    return render(request, 'main/index.html',)


def neiro_view(request):
    return render(request, 'main/press-single.html')


def finance_view(request):
    return render(request, 'main/single.html')
