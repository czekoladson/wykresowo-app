from django.urls import path
from . import views

app_name = 'earthquakes'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('age-plot', views.age_plot, name = 'age_plot'),
    path('info', views.info, name = 'info'),
    path('earthquakes', views.earthquakes, name = 'earthquakes'),
    path('air-plot', views.air_plot, name = 'air_plot'),
]
