from django.urls import path
from . import views
from . import views as MUseoApp_views

urlpatterns = [
    path('', views.home, name='home'),
    path('MUseoApp/', MUseoApp_views.as_view(), name='MUseoApp'),
]