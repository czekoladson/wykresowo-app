from django.urls import path
from . import views

app_name = 'earthquakes'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('plot', views.plot, name = 'plot'),
    path('info', views.info, name= 'info'),
]
