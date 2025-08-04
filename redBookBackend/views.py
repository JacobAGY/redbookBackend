from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    主页视图
    """
    return HttpResponse("""
    <h1>欢迎来到小红书后端系统</h1>
    <p>可用的API端点：</p>
    <ul>
        <li><a href="/admin/">管理后台</a></li>
        <li><a href="/user/user_list">用户列表</a></li>
        <li><a href="/product/product_list">产品列表</a></li>
    </ul>
    """) 