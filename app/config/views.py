from django.shortcuts import redirect


def index(request):

    #return HttpResponse('index')
    return  redirect('food:post_list')