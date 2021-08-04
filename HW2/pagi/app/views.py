from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv
from urllib.parse import urlencode, urljoin


# https://docs.djangoproject.com/en/3.1/topics/pagination/
# paginator = Paginator(all_articles, 2)
# current_page = request.GET.get('page', 1)
# articles = paginator.get_page(current_page)
# prev_page, next_page = None, None
# if articles.has_previous():
#     prev_page = articles.previous_page_number
# if articles.has_next():
#     next_page = articles.next_page_number
# context = { 'articles': articles, 'prev_page': prev_page, 'next_page': next_page, 'current_page': articles.number }
# return render(request, 'demo/articles.html',     context=context)

csv_path = settings.BUS_STATION_CSV
with open(csv_path, encoding="cp1251", newline='') as f:
    reader = csv.DictReader(f)
    all_data = list(reader)
p = Paginator(all_data, 10)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = request.GET.get("page", 1)
    bus_stations = p.page(current_page)
    prev_page_url, next_page_url = None, None
    main_url = reverse("bus_stations")
    if bus_stations.has_previous():
        prev_page_url = urljoin(main_url, "?" + urlencode({"page": bus_stations.previous_page_number()}))
        print(prev_page_url)
    if bus_stations.has_next():
        next_page_url = urljoin(main_url, "?" + urlencode({"page": bus_stations.next_page_number()}))
        print(next_page_url)
    return render(request, 'index.html', context={
        'bus_stations': bus_stations.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

