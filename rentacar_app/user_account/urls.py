from django.urls import path
from . import views


urlpatterns = [
    # path('change_password/', views.password_change_view, name='name_change_password'),
    # path('user_list/', views.UserListView.as_view(), name='name_user_list_view'),
    # path('<user_id>', views.delete_user_view, name='user-delete'),
    path('register/', views.register_view, name='register'),
    path('details/', views.register_view, name='details'),

]