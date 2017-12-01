import os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tjbaoan.settings")# project_name 项目名称
django.setup()

from tjbaoan.settings import BASE_DIR



if __name__ == '__main__':
    attrs = {
        '姓名': '',
        '性别': '',
        '年龄': '',
        '民族': '',
        '政治面貌': '',
        '籍贯': '',
        '身体状况': '',
        '身份证号': '',
        '婚姻状况': '',
        '毕业院校': '',
        '学历': '',
        '专业': '',
        '参加工作时间': '',
        '希望薪金/月': '',
        '联系方式': '',
        '家庭住址': '',
    }

    for key, val in attrs.items():
        print(key)
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
