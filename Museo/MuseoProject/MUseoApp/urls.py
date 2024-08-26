from django.urls import path
from . import views
from . import views as MUseoApp_views

urlpatterns = [
    path('', views.primera_vista, name='home'),
    path('MUseoApp/', MUseoApp_views.primera_vista, name='MUseoApp'),
]