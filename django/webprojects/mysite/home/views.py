from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return render(request, "main/home.html")

# 클래스의 경우
'''
class Index(View):
    def get(request):
        return render(request, "main/index.html")
'''