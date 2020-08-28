import datetime
from datetime import datetime
from django.conf import settings
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from .models import Info, active_countrie, all_countrie, world
from django.core.exceptions import ObjectDoesNotExist
import json
import os
import requests


def index(request):
    return HttpResponse('<h1>Hi, Welcome to Data page</h1>')


def update(request):
    json_data = requests.get(
        'https://covid19.who.int/page-data/index/page-data.json').json()
    counter1, counter2 = 0, 0

    for record in json_data["result"]["pageContext"]["rawDataSets"][
            "dayGroups"]:
        a = datetime.strptime(record["value"][0:10],
                              '%Y-%m-%d').strftime('%Y-%m-%d')
        for deeprecord in record["data"]["rows"]:
            b = str(deeprecord[0])
            c = str(deeprecord[1])
            d = int(deeprecord[2])
            e = int(deeprecord[3])
            f = int(deeprecord[7])
            g = int(deeprecord[8])

            if b != 'PS' and b != ' ':
                name = str(all_countrie.objects.get(coun_abr=b).coun)
                record_data = Info(day=a,
                                   country_abr=b,
                                   country=name,
                                   region=c,
                                   deaths=d,
                                   cum_deaths=e,
                                   confirmed=f,
                                   cum_confirmed=g)
                record_country = active_countrie(country_abr=b, country=name)

                if not Info.objects.filter(day=a,
                                           country_abr=b,
                                           country=name,
                                           region=c,
                                           deaths=d,
                                           cum_deaths=e,
                                           confirmed=f,
                                           cum_confirmed=g).exists():
                    record_data.save()
                    counter1 += 1

                if not active_countrie.objects.filter(country_abr=b,
                                                      country=name).exists():
                    record_country.save()
                    counter2 += 1

    for record in json_data["result"]["pageContext"]["rawDataSets"]["byDay"][
            "rows"]:
        a_time = record[0]
        a = datetime.fromtimestamp(a_time / 1000)
        a = datetime.strftime(a, '%Y-%m-%d')

        world_data = world(day=a,
                           deaths=int(record[1]),
                           cum_deaths=int(record[2]),
                           confirmed=int(record[6]),
                           cum_confirmed=int(record[7]))
        if not world.objects.filter(day=a,
                                    confirmed=int(record[1]),
                                    cum_confirmed=int(record[2]),
                                    deaths=int(record[6]),
                                    cum_deaths=int(record[7])).exists():
            world_data.save()

    return HttpResponse(
        str(counter1) + ' data added to list' + str(counter2) +
        ' countries added')

    # =========================================old json data format ==============================
    # url = 'https://dashboards-dev.sprinklr.com/data/9043/global-covid19-who-gis.json'
    # json_data = requests.get(url).json()

    # counter1 = 0
    # counter2 = 0

    # for row in json_data['rows']:
    #     a_time = row[0]
    #     a = datetime.datetime.fromtimestamp(a_time/1000)
    #     a = datetime.datetime.strftime(a, '%Y-%m-%d')
    #     b = str(row[1])
    #     c = str(row[2])
    #     d = int(row[3])
    #     e = int(row[4])
    #     f = int(row[5])
    #     g = int(row[6])

    #     check_country = all_countrie.objects.get(coun_abr=b)
    #     coun_name = check_country.coun
    #     record_data = Info(day=a, country_abr=b, country=coun_name, region=c,
    #                        deaths=d, cum_deaths=e, confirmed=f, cum_confirmed=g)
    #     record_country = active_countrie(country_abr=b, country=coun_name)

    #     if not Info.objects.filter(day=a, country_abr=b, country=coun_name, region=c, deaths=d, cum_deaths=e, confirmed=f, cum_confirmed=g).exists():
    #         # if b != 'PS':
    #             record_data.save()
    #             counter1 += 1
    #     if not active_countrie.objects.filter(country_abr=b, country=coun_name).exists:
    #         # if b != 'PS':
    #             record_country.save()
    #             counter2 += 1

    # return HttpResponse(str(counter1) + 'data added and ' + str(counter2) + ' countries added')

    # == == == == == == == == == == == == == == == ==Alt method by opening local csv file == == == == == == == == == == == == == ==
    # file = open('/home/mohit/Desktop/cov/data/cov_data.csv',
    #             newline='', encoding='utf-8-sig')

    # r = csv.reader(file)
    # header = next(r)
    # counter = 0
    # counter2 = 0

    # for each_item in r:
    #     a = datetime.strptime(each_item[0], '%Y-%m-%d')
    #     b = str(each_item[1])
    #     c = str(each_item[2])
    #     d = str(each_item[3])
    #     e = int(each_item[4])
    #     f = int(each_item[5])
    #     g = int(each_item[6])
    #     h = int(each_item[7])

    #     event = Info(day=a, country_abr=b, country=c, region=d,
    #                  deaths=e, cum_deaths=f, confirmed=g, cum_confirmed=h)
    #     event2 = country_data(country_abr=b, country=c)

    #     if not Info.objects.filter(day=a, country_abr=b, country=c, region=d,
    #                                deaths=e, cum_deaths=f, confirmed=g, cum_confirmed=h).exists():
    #         event.save()
    #         counter += 1

    #     if not country_data.objects.filter(country_abr=b, country=c).exists():
    #         event2.save()

    #         counter2 += 1

    # return HttpResponse(str(counter) + ' data added to list' + str(counter2) + ' countries added')
    # == == == == == == == == == == == == == == == == == == == == == == = end local csv file == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =


def detail_view(request, slug):
    try:
        country = active_countrie.objects.get(country_abr=slug)
        allCountry = active_countrie.objects.all().order_by('country')
        obj = Info.objects.filter(
            country_abr=country.country_abr).latest('day')
        datacab = Info.objects.filter(country_abr=slug)
        list1, list2, list3, list4, list5 = [], [], [], [], []
        for value in datacab:
            list1.append(value.day)
            list2.append(abs(value.deaths))
            list3.append(abs(value.confirmed))
            list4.append(abs(value.cum_confirmed))
            list5.append(abs(value.cum_deaths))

        return render(
            request, 'mysite/index2.html', {
                'country': obj,
                'day': list1,
                'deaths': list2,
                'confirmed': list3,
                'cum_confirmed': list4,
                'cum_deaths': list5,
                'allCountry': allCountry
            })

    except active_countrie.DoesNotExist:
        return render(request, 'mysite/404.html')


def upload_countries(request):
    file = open(os.path.join(settings.BASE_DIR, 'data/country_names.txt'), 'r')
    counter40 = 0
    for each_line in file:
        cn = each_line[0:2]
        ct = each_line[5:].strip()

        naya_desh = all_countrie(coun_abr=cn, coun=ct)

        if not all_countrie.objects.filter(coun_abr=cn, coun=ct).exists():
            naya_desh.save()
            counter40 += 1
    return HttpResponse(str(counter40) + ' added to the all country list')
