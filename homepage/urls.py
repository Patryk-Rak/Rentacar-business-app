from django.urls import path
from django.views.generic import TemplateView

app_name = 'home_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage/homepage.html'), name='home')
]
