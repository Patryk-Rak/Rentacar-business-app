from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import \
    (DetailView,
     ListView)
from django.core import serializers
from .filters import CarFilter
from .forms import CarsForm, CarsReservationHistoryForm
from .models import Cars, CarsReservationHistory
import io
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import CarsSerializer, CarsReservationHistorySerializer
# Create your views here.


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class CarsReservationHistoryViewSet(viewsets.ModelViewSet):
    queryset = CarsReservationHistory.objects.all()
    serializer_class = CarsReservationHistorySerializer


def car_filter(request):
    car_list = Cars.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    return render(request, 'cars/car_filter.html', {'filter': car_filter})


class Car_list_view(ListView):
    template_name = "cars/cars.html"
    model = Cars
    context_object_name = 'cars'
    paginate_by = 3
    filterset_class = CarFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


def cars_list(request):
    pg = Paginator(Cars.objects.all().order_by('year_of_production'), 2)
    page_number = request.GET.get('page')
    try:
        cars = pg.page(page_number)
    except EmptyPage:
        cars = pg.page(pg.num_pages)
    except PageNotAnInteger:
        cars = pg.page(1)
    return render(request, 'cars/cars.html', {'cars': cars})


@staff_member_required
def add_car(request):
    submitted = False
    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse("add-car"))
    else:
        form = CarsForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "cars/add_car.html", {'form': form, 'submitted': submitted})


class CarsDetailView(DetailView):
    template_name = "cars/cars_detail.html"

    # queryset = Cars.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cars, id=id_)


def search_car(request):
    if request.method == "POST":
        search = request.POST.get('car_search')
        # cars = Cars.objects.filter(mark=search)
        cars = Cars.objects.filter(Q(mark=search) | Q(model=search))
        return render(request, "cars/search_car.html", {'query': search, 'query_base': cars})
    else:
        return render(request, "cars/search_car.html", {})


@login_required(login_url="/user_account/login/")
def get_reservation_view(request, cars_id, *args, **kwargs):
    car = Cars.objects.get(pk=cars_id)
    if car.car_is_rented == False:
        # car.car_is_rented = 'Zarezerwowany'
        car.save()
        form = CarsReservationHistoryForm()
        if request.method == 'POST':
            form = CarsReservationHistoryForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                day1 = form.cleaned_data["day1"]
                day2 = form.cleaned_data["day2"]
                form.save(commit=True)
        return render(request, "cars/reservation.html", {'car': car,
                                                         'form': form})
    else:
        return HttpResponse("Auto jest wypozyczone")


def get_reservation_confirmed_view(request, cars_id):
    car = Cars.objects.get(pk=cars_id)
    form = CarsReservationHistoryForm()
    return render(request, 'cars/reservation_confirmed.html', {'car': car,
                                                               'form': form})


# @api_view(['POST'])
# def get_reservation_confirmed_view(request,):
#     # context = {}zz
#     calculated = CarsReservationHistory.objects.all()
#     # car = Cars.objects.all()
#     if request.method == "POST":
#         # form = CarsReservationHistoryForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             day1 = form.cleaned_data["day1"]
#             day2 = form.cleaned_data["day2"]
#             form.save(commit=True)
#             # serializer = CarsReservationHistorySerializer(data=request.data)
#             # if serializer.is_valid():
#             #     serializer.save()
#                 return Response(serializer.data)
#     else:
#         form = CarsReservationHistoryForm()
#     return render(request, "cars/reservation_confirmed.html",
#                   {"form": form, "calculated": calculated, "car":car, })
#             # CarsReservationHistoryForm.day_started = form.cleaned_data.get("day_started")
#             # CarsReservationHistoryForm.day_ended = form.cleaned_data.get("day_ended")
#             # return redirect("http://127.0.0.1:8000/")
#         else:
#             # context['registration_form'] = form
#             return HttpResponse("Huj bombelki nie dziala")
# # def update_view(request, cars_id ):
#     car = Cars.objects.get(pk=cars_id)
#     return render(request, 'cars/cars_info_update.html', {'car':car})

@staff_member_required
def update_view(request, cars_id):
    car = Cars.objects.get(pk=cars_id)
    form = CarsForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('cars')
    return render(request, 'cars/cars_info_update.html',
                  {'car': car,
                   'form': form
                   })


# @login_required(login_url="/user_account/login/")
# def get_reservation_view(request, cars_id):
#     car = Cars.objects.get(pk=cars_id)
#     form = CarsReservationHistoryForm()
#     if car.car_is_rented == False:
#         form = CarsReservationHistoryForm(request.POST, request.FILES)
#         # day1 = form.cleaned_data.get("day1")
#         # day2 = form.cleaned_data.get["day2"]
#         if form.is_valid():
#             form.save()
#             car.save()
#             CarsReservationHistory.day1 = form.cleaned_data.get["day1"]
#             CarsReservationHistory.day2 = form.cleaned_data.get["day2"]
#         return render(request, 'cars/reservation.html', {form: 'form',
#                                                          car: 'car'})
#     else:
#         return HttpResponse("Test")
def hello(request, cars_id):
    car = Cars.objects.get(pk=cars_id)
    return HttpResponse(f'Hello !!!! Now is '[CarsReservationHistory.convert_date(self=get_reservation_confirmed_view(request))])