from django.urls import path
from . import views
urlpatterns = [
    path('', views.Car_list_view.as_view(), name="cars"),
    path('add_car/', views.add_car, name='add-car'),
    path('search_car/', views.search_car, name='search-car'),
    path('filter_car/', views.car_filter, name='car-filter'),
    path('cars/<cars_id>', views.get_reservation_view, name='car-reservation'),
    path('<cars_id>/', views.update_view, name='car-update'),
    path('<int:id>/', views.CarsDetailView.as_view(), name='cars_detail'),
    # path('<event/int:id>/', views.add_event_views, name='add-event')

]