import os

from django.contrib.auth import login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django import forms
from tjbaoan import settings
from tjbaoan.settings import CONTACT_TEL, COMPANY_NAME, ABOUT_US, STATIC_FOR_VIEW
from tools.itools import itools
from website.models import Info, User


class LogForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '用户名', 'required': 'required', }),
                               max_length=50, error_messages={'required': 'username不能为空', })
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '密 码', 'required': 'required', }),
        max_length=20, error_messages={'required': 'password不能为空', })



# 定义检测登录的装饰器
def check_login(func):
    def wrapper(request, *args, **kwargs):
        # print('in wrapper')
        if request.user.is_authenticated():
            # return HttpResponseRedirect('/login/')
            # print('shi')
            return func(request, *args, **kwargs)
        else:
            # print('fou')
            return redirect('/login/')
    return wrapper


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

def do_logout(request):
    try:
        if request.user.is_authenticated():
            logout(request)
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponse("<script>alert('你还没有登录');window.history.back(-1);</script>")
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/index/')
@csrf_exempt
def do_login(request):
    login_user = request.user.username
    ret = {
        'title': '登录',
        'login_user': login_user,
        'error': '',
    }



    lf = LogForm()
    ret['lf'] = lf

    if request.method == 'POST':
        checkForm = LogForm(request.POST)
        if checkForm.is_valid():
            print(checkForm.cleaned_data['username'], checkForm.cleaned_data['password'])
            try:
                user = User.objects.get(username=checkForm.cleaned_data['username'])
                if user.check_password(checkForm.cleaned_data['password']):
                    print('passwd:{}'.format(checkForm.cleaned_data['password']))
                    login(request, user)
                    return HttpResponse("<script>alert('登录成功');window.location.href='/userfuncs/';</script>")
                else:
                    ret['error'] = '帐号或密码错误，请重新输入。'
                    ret['lf'] = checkForm

            except Exception as e:
                print(e)
                ret['error'] = '帐号或密码错误，请重新输入。'
                ret['lf'] = checkForm

        else:
            errobj = checkForm.errors
            print(type(errobj))

            es = checkForm.errors.as_json()
            print(type(es))
            err = es.split('"')[-2]
            print(err)
            ret['error'] = err
            ret['lf'] = checkForm


    if request.method == 'POST':
        print(request.POST)




    return render(request, 'login.html', ret)





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

@check_login
def info(request):
    login_user = request.user.username
    ret = {
        'title': '信息列表',
        'login_user': login_user,
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

@check_login
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


@check_login
def userfuncs(request):
    login_user = request.user.username
    ret = {
        'title': '用户页面',
        'login_user': login_user,
    }


    if request.method == 'GET':
        act = request.GET.get('act')
        if act == 'logout':
            do_logout(request)
            return HttpResponseRedirect('/index/')
            # return HttpResponse('logout')



    return render(request, 'userfuncs.html', ret)