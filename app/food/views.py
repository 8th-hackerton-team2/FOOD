from django.shortcuts import render
from food.models import Pension
from .pension_crawler import pension_crawler,pension_detail_cralwer

def post_list(request):
    pension_crawler()
    pensions = Pension.objects.all()

    context = {
        'pensions': pensions,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request,pk):
    pensions = Pension.objects.get(pk=pk)
    pension = pension_detail_cralwer(pensions.pldx)
    context ={
        'pension': pension,
    }
    return render(request, 'posts/post_detail.html', context)