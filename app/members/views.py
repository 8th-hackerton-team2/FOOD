from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import login, get_user_model, logout
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


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    print(request)
    return redirect('members:post_list')





def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST,request.FILES)

        # form에 들어있는 데이터가 유효한지 검사.(해당 form 클래스에서 정의한 데이터 형식에서 벋어나지 않는지 판단.)
        if form.is_valid():

            user = form.signup() #signup 메소드는 form의 메소드 인데 form은 signupForm클래스의 인스턴스이다.

            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('members:post_list')

    else:
        form = SignupForm()

    context = {'form': form, }
    return render(request, 'members/signup.html', context)

