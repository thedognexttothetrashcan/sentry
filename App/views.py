from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    a = 123
    # try:
    #     a = 50 / 0
    # except:
    #     print('sadasd')
    return HttpResponse('测试成功：')