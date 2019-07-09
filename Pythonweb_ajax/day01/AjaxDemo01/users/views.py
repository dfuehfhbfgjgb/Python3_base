from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
import json
from django.core import serializers


# 注册
def register(request):
    return render(request, 'users/register.html')


def is_name(request):
    uname = request.GET['uname']
    try:
        user = models.User.objects.get(uname=uname)
        return HttpResponse('1')
    except:
        return HttpResponse('0')


def createuser(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    nickname = request.POST['nickname']
    try:
        models.User.objects.create(
            uname=uname,
            upwd=upwd,
            nickname=nickname
        )

        return HttpResponse('注册成功')
    except:
        return HttpResponse('注册失败')


def query_users(request):
    return render(request, 'users/query.html')


def query_server(request):
    temp = ''
    users = models.User.objects.all()
    for user in users:
        # temp += user.id+'_'+user.uname+'_'+\
        #         user.upwd+'_'+user.nickname+'|'
        temp += "%s_%s_%s_%s|" % \
                (user.id, user.uname, user.upwd, user.nickname)
    msg = temp[0:-1]
    return HttpResponse(msg)


def jso(request):
    return render(request, 'users/jso.html')


def json_views(request):
    return render(request, 'users/json.html')


def json_server(request):
    # 1.通过字典来模拟单个对象
    dic = {
        'uname': 'laodu',
        'uage': 11,
        'ugender': 'male'
    }
    # 2.通过列表加字典模拟多个对象
    lis = [
        {'uname': 'laodu', 'uage': 18, 'ugender': 'male'},
        {'uname': 'laoxu', 'uage': 28, 'ugender': 'male'},
        {'uname': 'laozuo', 'uage': 8, 'ugender': 'male'}
    ]
    # 3.读取数据库中的数据并转换成字符串
    users = models.User.objects.all()
    jsonStr = serializers.serialize('json', users)
    # jsonStr = json.dumps(str)
    return HttpResponse(jsonStr)


def user_server(request):
    users = models.User.objects.all();
    jsonStr = serializers.serialize('json', users)
    return HttpResponse(jsonStr)


def front_json(request):
    return render(request,'users/front_json.html')


def front_server(request):
    jsonStr = request.GET['params']
    # print(jsonStr)
    # 通过json.loads（）将jsonStr转换为python字典
    dic = json.loads(jsonStr)
    msg = "姓名："+dic['uname']+"  年龄："+str(dic['uage'])+\
          "  性别："+dic['ugender']
    return HttpResponse(msg)