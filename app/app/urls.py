
from django.contrib import admin
from django.urls import path, include 
from core import views




urlpatterns = [
    path('admin/', admin.site.urls),

    path('' , views.landing_page , name='landing_page' ),
    
    ]
