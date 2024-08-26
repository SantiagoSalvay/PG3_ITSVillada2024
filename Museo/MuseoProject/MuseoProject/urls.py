from django.contrib import admin
from django.urls import path, include
from MUseoApp import views as MUseoApp_views  

urlpatterns = [
    path('', MUseoApp_views.home, name='home'),  
    path('MUseoApp/', include('MUseoApp.urls')),        
    path('admin/', admin.site.urls),          
]