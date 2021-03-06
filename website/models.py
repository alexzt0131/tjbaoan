import datetime
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):     #继承AbstractUser
    desc = models.TextField()





class Info(models.Model):
    # attrs = (
    #     '姓名',
    #     '性别',
    #     '年龄',
    #     '民族',
    #     '政治面貌',
    #     '籍贯',
    #     '身体状况',
    #     '身份证号',
    #     '婚姻状况',
    #     '毕业院校',
    #     '学历',
    #     '专业',
    #     '参加工作时间',
    #     '希望薪金/月',
    #     '联系方式',
    #     '家庭住址',
    # )
    # name = models.CharField(max_length=150, null=True, blank=True, verbose_name='姓名')
    name = models.CharField(max_length=150, default='', verbose_name='姓名')
    sex = models.CharField(max_length=150, default='', verbose_name='性别')
    age = models.CharField(max_length=150, default='', verbose_name='年龄')
    ethnic = models.CharField(max_length=150, default='', verbose_name='民族')
    political_role = models.CharField(max_length=150, default='', verbose_name='政治面貌')
    native_place = models.CharField(max_length=150, default='', verbose_name='籍贯')
    health = models.CharField(max_length=150, default='', verbose_name='身体状况')
    PID = models.CharField(max_length=150, default='', verbose_name='身份证号')
    marital_status = models.CharField(max_length=150, default='', verbose_name='婚姻状况')
    graduate_institutions = models.CharField(max_length=150, default='', verbose_name='毕业院校')
    education_background = models.CharField(max_length=150, default='', verbose_name='学历')
    major = models.CharField(max_length=150, default='', verbose_name='专业')
    timeofwork = models.CharField(max_length=150, default='', verbose_name='参加工作时间')
    wished_salary = models.CharField(max_length=150, default='', verbose_name='希望薪金/月')
    contact = models.CharField(max_length=150, default='', verbose_name='联系方式')
    addr = models.CharField(max_length=150, default='', verbose_name='家庭住址')
    wanttosay = models.TextField(max_length=300, null=True, blank=True, verbose_name='自我描述')
    uuid = models.UUIDField(default=uuid.uuid4, null=False, verbose_name='uuid')
    create_date = models.CharField(max_length=40, default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), verbose_name='创建时间')


    def __str__(self):
        return '{} {}-{}-{}-{}-{}-{}'.format(self.create_date, self.name, self.sex, self.age, self.education_background, self.graduate_institutions, self.wished_salary)