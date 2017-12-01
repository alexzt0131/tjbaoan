import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from tjbaoan import settings
from tjbaoan.settings import CONTACT_TEL, COMPANY_NAME, ABOUT_US, STATIC_FOR_VIEW
from tools.itools import itools
from website.models import Info


def global_settings(request):
    '''
    此函数用来提供给模板中直接调用settings中的全局变量
    需要在settings TEMPLATES 中添加此函数
    'security.views.global_settings',
    :param request:
    :return:
    '''
    return {
        'CONTACT_TEL': settings.CONTACT_TEL,
    }



@csrf_exempt
def regist(request):
    ret ={}

    attrs = (
        '姓名',
        '性别',
        '年龄',
        '民族',
        '政治面貌',
        '籍贯',
        '身体状况',
        '身份证号',
        '婚姻状况',
        '毕业院校',
        '学历',
        '专业',
        '参加工作时间',
        '希望薪金/月',
        '联系方式',
        '家庭住址',
    )
    ret['attrs'] = attrs


    if request.method == 'POST':
        # print(request.POST)
        request_attrs = request.POST
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

        result = []
        for key, val in attrs.items():
            attrs[key] = request_attrs[key]


        Info.objects.create(
            name=attrs['姓名'].strip(),
            sex=attrs['性别'].strip(),
            age=attrs['年龄'].strip(),
            ethnic=attrs['民族'].strip(),
            political_role=attrs['政治面貌'].strip(),
            native_place=attrs['籍贯'].strip(),
            health=attrs['身体状况'].strip(),
            PID=attrs['身份证号'].strip(),
            marital_status=attrs['婚姻状况'].strip(),
            graduate_institutions=attrs['毕业院校'].strip(),
            education_background=attrs['学历'].strip(),
            major=attrs['专业'].strip(),
            timeofwork=attrs['参加工作时间'].strip(),
            wished_salary=attrs['希望薪金/月'].strip(),
            contact=attrs['联系方式'].strip(),
            addr=attrs['家庭住址'].strip(),
        )

        return HttpResponse("<script>alert('信息已成功提交');window.location.href='/index';</script>")

        return HttpResponse('信息已成功提交。(js为启用)')




    return render(request, 'regist.html', ret)
def index(request):

    ret = {
        'tel': CONTACT_TEL,
        'com_name': COMPANY_NAME,
        'about_us': ABOUT_US,
        'title': 'title'
    }

    rootdir = STATIC_FOR_VIEW + '/images/xuanchuan/'  # 指明被遍历的文件夹
    # rootdir = STATIC_ROOT + '/images/xuanchuan/'  # 指明被遍历的文件夹
    # print(rootdir)
    # print(os.path.exists(rootdir))
    file_names = itools.retrive(rootdir=rootdir)['files']

    ret['file_names'] = file_names
    return render(request, 'index.html', ret)

def join_us(request):
    # return HttpResponse('asdf')
    ret = {}
    with open(STATIC_FOR_VIEW + '/docs/zhaopin.txt') as f:
        lines = f.readlines()
    ret['lines'] = lines
    return render(request, 'joinus.html', ret)


def info(request):
    ret = {
        'title': '信息列表'
    }
    infos = Info.objects.all().order_by('-create_date')

    paginator = Paginator(infos, 10)

    try:
        page = int(request.GET.get('page', 1))  # 1是没有数据的默认值
        print('page = {}'.format(page))
        infos = paginator.page(page)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        infos = paginator.page(1)

    ret['pages'] = infos.paginator.num_pages
    ret['count'] = infos.paginator.count


    ret['infos'] = infos
    return render(request, 'infos.html', ret)


def detail(request):
    ret = {
        'title': '详细信息'
    }
    if request.method == 'GET':
        uuid = request.GET.get('uuid')
        information = Info.objects.get(uuid=uuid)

        retinfo = (
            ('姓名', information.name),
            ('性别', information.sex),
            ('年龄', information.age),
            ('民族', information.ethnic),
            ('政治面貌', information.political_role),
            ('籍贯', information.native_place),
            ('身体状况', information.health),
            ('身份证号', information.PID),
            ('婚姻状况', information.marital_status),
            ('毕业院校', information.graduate_institutions),
            ('学历', information.education_background),
            ('参加工作时间', information.timeofwork),
            ('希望薪金 / 月', information.wished_salary),
            ('联系方式', information.contact),
            ('家庭住址', information.addr),
        )



        ret['info'] = retinfo

    return render(request, 'detail.html', ret)