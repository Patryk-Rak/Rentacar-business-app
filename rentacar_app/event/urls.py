
from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.add_event_views, name='add_event'),

    ]