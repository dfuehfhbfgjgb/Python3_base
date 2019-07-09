from django.http import HttpResponse
from django.shortcuts import render

def xhr_views(request):
    return render(request,'01-xhr.html')

def ajax_get(request):
    return render(request,'02-ajax-get.html')

def server02(request):
    return HttpResponse("这是使用AJAX发送的请求")

def server02_param(request):
    #接收前端传递过来的参数 - uname
    uname = request.GET['uname']
    return HttpResponse("Welcome:" + uname)













