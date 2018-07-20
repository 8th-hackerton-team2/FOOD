from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.




from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from members.forms import SignupForm

User = get_user_model()

__all__=(
    'post_list',
    'login_view',
    # 'signup',

)


def post_list(request):
    return render(request, 'posts/post_list.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET['next'])
            return redirect('members:post_list')
        else:
            return redirect('members:login')
    else:
        return render(request, 'members/login.html')


# def signup(request):
#
#     if request.method == 'POST':
#         form = SignupForm(request.POST,request.FILES)
#         if form.is_valid():
#             user = form.signup()
#             login(request,user)
#             return redirect('index')
#     else:
#         form = SignupForm()
#
#     context = {'form': form, }
#     return render(request, 'members/signup.html', context)
#
