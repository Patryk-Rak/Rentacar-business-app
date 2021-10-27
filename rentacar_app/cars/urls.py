from django.urls import path, include
from . import views
from rest_framework import routers
from django.urls import include, path
from .views import CarsViewSet, CarsReservationHistoryViewSet

router = routers.DefaultRouter()

router.register(r'student', CarsViewSet)
router.register(r'cars', CarsReservationHistoryViewSet)

app_name = 'main_app'

urlpatterns = [
    path('', views.Car_list_view.as_view(), name="cars"),
    path('add_car/', views.add_car, name='add-car'),
    path('search_car/', views.search_car, name='search-car'),
    path('filter_car/', views.car_filter, name='car-filter'),
    path('cars/<cars_id>', views.get_reservation_view, name='car-reservation'),
    path('<cars_id>/x', views.update_view, name='car-update'),
    path('<int:id>/x', views.CarsDetailView.as_view(), name='cars_detail'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


