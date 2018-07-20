
# admin /특정비밀번호
# 위 값으로 로그인 시도시 authenticate가 성송하도록 커스텀 Backend를 작성
# members.backends모듈에 작성
# Backend 명은 Settings.Backend
# password는 장고안의 문자열을 생성해서? 써야함.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class SettingsBackend:
    '''
    ADMIN = 'admin'
    ADMIN_PASSWORD ='pbkdf2_sha256$100000$zNIjdY5qwrae$dASPtmQ/vw7VQ9cFD69aYu7hTxTLQLoFFzLqUzxtq1I='
    '''

    def authenticate(self, request, username=None,password=None):
        login_valid = (settings.ADMIN_USERNAME == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)

        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None