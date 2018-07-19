import json
import os

from django.core.management.base import BaseCommand, CommandError

from config.settings.base import SECRET_DIR
from django.contrib.auth import get_user_model # 슈퍼유저 생성 위해 이것 가져와야 한다.


# admin /특정비밀번호
# 위 값으로 로그인 시도시 authenticate가 성송하도록 커스텀 Backend를 작성
# members.backends모듈에 작성
# Backend 명은 Settings.Backend
# password는 장고안의 문자열을 생성해서? 써야함.



class Command(BaseCommand):
    help = 'Createing super user'

    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):

        User = get_user_model()
        secrets = json.load(open(os.path.join(SECRET_DIR, 'production.json')))
        superuser = secrets["SUPERUSER"]

        username = superuser["USERNAME"]
        email = superuser["EMAIL"]
        password = superuser["PASSWORD"]
        #
        #
        # # 유저가 하나라도 있나 검사하는 플레그
        # ANY_USER_EXISTS_FLAG = User.objects.all()!=0
        # # 슈퍼유저가 있는지 모든 유저 돌면서 검사하기 위한 플래그
        # SUPER_USER_EXISTS_FLAG = False
        #
        # if ANY_USER_EXISTS_FLAG:
        #     for user in User.objects.all():
        #         if user.is_superuser ==True:
        #             SUPER_USER_EXISTS_FLAG =True
        #             break
        #
        # # 아무 유저도 없거나 유저가 있더라도 슈퍼유저가 아닐경우 둘중하나라도 포함되면
        # if ANY_USER_EXISTS_FLAG==False or  SUPER_USER_EXISTS_FLAG == False:
        #     User.objects.create_superuser(
        #         username=username, password=password, email=email)

        #
        # 일차적인 방법.
        if not User.objects.filter(username=superuser['USERNAME']).exists():
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
            )

        # 위와 같은 경우에는 관리자 비번 등을 계속해서 유지해햐 한다. 제이슨 파일 없이 settings이용해서 백엔드 만들 수 있다.
        # 커멘드로 직접 만드는것 말고 만들어보자.

        from members.backends import SettingsBackend

