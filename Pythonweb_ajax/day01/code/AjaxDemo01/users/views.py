from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def register_views(request):
    return render(request,'register.html')

def checkuname(request):
  #1.获取前端传递过来的参数-uname
  uname = request.GET['uname']
  #2.查询数据库中user表uname列中是否存在 uname 对应的值
  users = User.objects.filter(uname=uname).all()
  #3.根据查询结果给出响应
  if users:
    return HttpResponse("用户名称已存在")
  
  return HttpResponse("通过")