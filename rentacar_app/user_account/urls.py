from django.urls import path
from . import views
from django.conf.urls import include

app_name = "account"

urlpatterns = [
    path('<user_id>/', views.account_view, name="view"),
    path('<user_id>/edit/', views.edit_account_view, name="edit"),
]