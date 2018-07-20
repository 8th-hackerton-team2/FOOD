from django.shortcuts import render
from food.models import Pension


def post_list(request):
    pensions = Pension.objects.all()

    context = {
        'pensions': pensions,
    }
    return render(request, 'posts/post_list.html', context)