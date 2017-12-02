import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tjbaoan.settings")# project_name 项目名称
django.setup()

from django.contrib.auth.hashers import make_password

from website.models import User
from tjbaoan.settings import BASE_DIR



if __name__ == '__main__':
    # user = User.objects.create(username='alex'],
    #                            email=checkForm.cleaned_data['email'],
    #                            password=make_password(checkForm.cleaned_data['password']))
    # user.save()
    username = 'tjanbao'
    password = 'tjanbao'
    try
    flag = User.objects.get(username=username)
    print(flag)
    pass

    # with open(STATICFILES_DIRS[0] + '/docs/zhaopin.txt') as f:
    #     lines = f.readlines()
    #
    #
    # for i in lines:
    #     print(i)
    # rootdir = STATICFILES_DIRS[0] + '/images/xuanchuan/'  # 指明被遍历的文件夹
    # print(rootdir)
    #
    # print(os.path.exists(rootdir))
    # file_names = []
    # file_names = itools.retrive(rootdir=rootdir)['files']
    #
    # print(file_names)
