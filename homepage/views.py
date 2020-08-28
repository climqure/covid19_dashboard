from django.shortcuts import render
from django.http import Http404
from data.models import active_countrie, world
# from django.http import HttpResponse

# Create your views here.


def index(request):
    allCountry = active_countrie.objects.all().order_by('country')
    list1, list2, list3, list4, list5 = [], [], [], [], []
    obj = world.objects.latest('day')
    obj.country = "Global Covid-19 Figures"
    obj.country_abr = "All"
    datacab = world.objects.all()

    for value in datacab:
        list1.append(value.day)
        list2.append(value.deaths)
        list3.append(value.confirmed)
        list4.append(value.cum_confirmed)
        list5.append(value.cum_deaths)

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


def handler404(request, exception):
    context = {}
    return render(request, "mysite/404.html", context)


def handler500(request, exception):
    context = {}
    return render(request, "mysite/404.html", context)