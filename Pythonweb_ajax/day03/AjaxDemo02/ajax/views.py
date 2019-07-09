from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.


def load_views(request):
    return render(request, '01-load.html')


def server01(request):
    # 接收前端传递过来的参数
    uname = request.POST['uname']
    uage = request.POST['uage']
    return render(request, '01-server.html', locals())


def get_views(request):
    return render(request, '02-get.html')


def server02(request):
    dic = {
        'uname': '杜怡围',
        'uage': 10,
    }
    jsonStr = json.dumps(dic)
    return HttpResponse(jsonStr)


def post_views(request):
    return render(request, '03-post.html')


def server03(request):
    uname = request.POST['uname']
    uage = request.POST['uage']
    ugender = request.POST['ugender']
    msg = "姓名:" + uname + " 年龄:" + str(uage) + " 性别:" + ugender
    print(uname, uage, ugender)
    return HttpResponse(msg)


def ajax_views(request):
    return render(request, '04-ajax.html')


def server04(request):
    list = [
        {
            "cname": "Python",
            "teacher": "laodu"
        },
        {
            "cname": "体育",
            "teacher": "xiaodu"
        }
    ]
    return HttpResponse(json.dumps(list))


def cross_views(request):
    return render(request, '05-cross.html')


def server05(request):
    return HttpResponse("这是server05响应回来的内容")


def js_views(request):
    return render(request, '06-js.html')


def server06(request):
    func = request.GET['callback']
    return HttpResponse(func+"('这是server06响应的内容');")
