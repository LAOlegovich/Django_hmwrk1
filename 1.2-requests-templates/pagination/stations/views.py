from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get("page",1)
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile)
        list_of_data = [row for row in data]
    print(list_of_data)

    pagi = Paginator(list_of_data,20)
    page = pagi.get_page(int(page_number))
            
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
         'bus_stations':page,
         'page': page
    }
    return render(request, 'stations/index.html', context)
