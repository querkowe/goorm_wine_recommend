from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    context = "추천 기능"

    return render(request, 'recommand/index.html')


# title 을 받아서 처리할 함수
def detail(request): 

    title = request.POST['title']
    
    print (title)
    return render(request, 'recommand/detail.html', {'title':title})



def recommand (request):
    return HttpResponse('추천 기능 구현 웹페이지')
    