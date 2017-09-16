from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import View

from .models import Car, CarMaker


class IndexView(View):
    def get(self, request):
        return render(request, 'car/index.html', {'section': 'index'})


def dashboard(request):
    return render(request, 'car/dashboard.html')


def car_detail(request):
    # car = get_object_or_404(Car, id=car_id)
    car = Car.objects.get(pk=12)
    # car = get_object_or_404(Car, id=car_id)
    return render(request, 'car/car_detail.html', {'car': car})


def car_maker_detail(request, maker_id):
    car_maker = get_object_or_404(CarMaker, id=maker_id)
    return render(request, 'car/car_maker_detail.html', {'car_maker': car_maker})


def car_list(request):
    cars = Car.objects.all().order_by('car_name')
    paginator = Paginator(cars, 25)
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cars = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cars = paginator.page(paginator.num_pages)

    return render(request, 'car/car_list.html',
                  {'cars': cars}
                  )


def car_maker_list(request):
    car_makers = CarMaker.objects.all().order_by('car_maker')
    paginator = Paginator(car_makers, 25)
    page = request.GET.get('page')
    try:
        car_makers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car_makers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car_makers = paginator.page(paginator.num_pages)

    return render(request, 'car/car_list.html',
                  {'car_makers': car_makers}
                  )
