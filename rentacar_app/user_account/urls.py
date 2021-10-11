from django.urls import path
from . import views
from django.conf.urls import include

app_name = "account"

urlpatterns = [
    # path('user_list/', views.UserListView.as_view(), name='name_user_list_view'),
    path('<user_id>/', views.account_view, name="view"),
]