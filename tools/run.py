import os, django

from security.tools.itools import itools

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "security_tj.settings")# project_name 项目名称
django.setup()



from security_tj.settings import STATICFILES_DIRS, BASE_DIR

if __name__ == '__main__':
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
