import os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tjbaoan.settings")# project_name 项目名称
django.setup()

from tjbaoan.settings import BASE_DIR



if __name__ == '__main__':
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    print(STATIC_ROOT)
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
