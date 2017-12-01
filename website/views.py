import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from tjbaoan import settings
from tjbaoan.settings import CONTACT_TEL, COMPANY_NAME, ABOUT_US, STATIC_FOR_VIEW
from tools.itools import itools


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