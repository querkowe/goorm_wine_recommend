from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .image import scrape

# Create your views here.
def index(request):

    context = "추천 기능"

    return render(request, 'recommand/index.html')


# title 을 받아서 처리할 함수
def detail(request):

    title = request.POST.get('title')
    grade = request.POST.get('grade')
    main_item = {'aging':'None'}
    recommanded = []

    if grade == '1':
        main_item = WineFirst.objects.get(aging=title)
        recom_idx = CosFirst.objects.get(id=main_item.id)

        recommanded.append(WineFirst.objects.get(id=recom_idx.recommand_1).aging)
        recommanded.append(WineFirst.objects.get(id=recom_idx.recommand_2).aging)
        recommanded.append(WineFirst.objects.get(id=recom_idx.recommand_3).aging)
    elif grade == '2':
        main_item = WineSecond.objects.get(aging=title)
        recom_idx = CosSecond.objects.get(id=main_item.id)

        recommanded.append(WineSecond.objects.get(id=recom_idx.recommand_1).aging)
        recommanded.append(WineSecond.objects.get(id=recom_idx.recommand_2).aging)
        recommanded.append(WineSecond.objects.get(id=recom_idx.recommand_3).aging)
    elif grade == '3':
        main_item = WineThird.objects.get(aging=title)
        recom_idx = CosThird.objects.get(id=main_item.id)

        recommanded.append(WineThird.objects.get(id=recom_idx.recommand_1).aging)
        recommanded.append(WineThird.objects.get(id=recom_idx.recommand_2).aging)
        recommanded.append(WineThird.objects.get(id=recom_idx.recommand_3).aging)

    image = scrape(f"{main_item.variety}  {title}")

    return render(request, 'recommand/detail.html', {'main_item':main_item, 'recommand':recommanded, 'image':image})



def recommand (request):
    return HttpResponse('추천 기능 구현 웹페이지')
