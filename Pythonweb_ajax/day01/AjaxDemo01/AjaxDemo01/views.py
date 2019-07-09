from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def xhr_views(request):
    return render(request, '01-xhr.html')


def ajax_get(request):
    return render(request, '02-ajax-get.html')


def server02(request):
    return HttpResponse("这是使用AJAX发送的请求")


def server02_param(request):
    # 接收前端传递过来的参数 - uname
    uname = request.GET['uname']
    active = request.GET['active']
    return HttpResponse("Welcome:" + uname + ' ' + active)


def ajax_post(request):
    return render(request, '03-ajax-post.html')


def server03(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    return HttpResponse("用户名：%s,密码：%s" % (uname, upwd))
