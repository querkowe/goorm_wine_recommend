from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .image import scrape
import json
import urllib.parse

# Create your views here.
def main(request):


    return render(request, 'recommand/index.html')


def index(request):

    wine_titles = []
    wine_maps = {}
    for wine in list(WineName.objects.all()):
        wine_maps[wine.title] = wine.grade
        wine_titles.append(wine.title)
    return render(request, 'recommand/recommand.html', {'wine_titles': wine_titles, 'wine_maps':json.dumps(wine_maps)})
    # return render(request, 'recommand/index.html', {'wine_titles': wine_titles})


# title 을 받아서 처리할 함수
def detail(request):

    title = request.POST.get('title')
    grade = int(request.POST.get('grade'))
    print('input : ', title, grade)
    print('keys : ', list(request.POST.keys()))
    main_item = {'aging':'None'}
    recommanded = []

    if grade == 1:
        # main_item = list(WineFirst.objects.filter(aging=title))[0]
        main_item = WineFirst.objects.filter(aging=title)[:1][0]
        recom_idx = CosFirst.objects.get(id=main_item.id)

        recommanded.append(WineFirst.objects.get(id=recom_idx.recommand_1).aging)
        recommanded.append(WineFirst.objects.get(id=recom_idx.recommand_2).aging)
        recommanded.append(WineFirst.objects.get(id=recom_idx.recommand_3).aging)
    elif grade == 2:
        # main_item = list(WineSecond.objects.filter(aging=title))[0]
        main_item = WineSecond.objects.filter(aging=title)[:1][0]
        recom_idx = CosSecond.objects.get(id=main_item.id)

        recommanded.append(WineSecond.objects.get(id=recom_idx.recommand_1).aging)
        recommanded.append(WineSecond.objects.get(id=recom_idx.recommand_2).aging)
        recommanded.append(WineSecond.objects.get(id=recom_idx.recommand_3).aging)
    elif grade == 3:
        # main_item = list(WineThird.objects.filter(aging=title))[0]
        main_item = WineThird.objects.filter(aging=title)[:1][0]
        recom_idx = CosThird.objects.get(id=main_item.id)

        recommanded.append(WineThird.objects.get(id=recom_idx.recommand_1).aging)
        recommanded.append(WineThird.objects.get(id=recom_idx.recommand_2).aging)
        recommanded.append(WineThird.objects.get(id=recom_idx.recommand_3).aging)

    glink = f"https://www.vivino.com/search/wines?q={str(urllib.parse.quote_plus(title))}"

    image = scrape(f"wine {title}  {main_item.variety}")
    # slink, image = scrape(glink)
    # image = '#'


    return render(request, 'recommand/result.html', {'main_item':main_item, 'recommand':recommanded, 'image': image, 'glink': glink})

# def autocomplete(request):
#     grade = request.POST.get('grade')
#     query = request.POST.get('title', None)
#
#     schema = None
#
#     if grade == '1':
#         schema = WineFirst
#     elif grade == '2':
#         schema = WineSecond
#     elif grade == '3':
#         schema = WineThird
#
#     candidate = list(schema.objects.filter(aging__icontains=query)[:10])
#
#     return JsonResponse({'candid': candidate})

def recommand (request):
    return HttpResponse('추천 기능 구현 웹페이지')
