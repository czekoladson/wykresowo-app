from django.shortcuts import render
from earthquakes.models import PersonSalary, CityAir
import plotly.express as px

def index(request):
    return render(request, 'earthquakes/index.html')

def info(request):
    return render(request, 'earthquakes/info.html')

def earthquakes(request):
    return render(request, 'earthquakes/earthquakes.html')

def age_plot(request):
    person_salaries = PersonSalary.objects.all()
    ages = person_salaries.values_list('age', flat = True)
    salaries = person_salaries.values_list('salary', flat = True)
    fig = px.bar(
        x = ages,
        y = salaries,
        title = "Wypłata Względem Wieku",
        height = 800,
    )
    html0 = fig.to_html()
    context = {'chart0': html0}
    return render(request, 'earthquakes/scatter.html', context)

def air_plot(request):
    air_quality = CityAir.objects.all()
    cities = air_quality.values_list('city', flat=True)
    air_qualities = air_quality.values_list('airquality', flat=True)

    fig = px.bar(
        x = cities,
        y = air_qualities,
        title = "Jakość Powetrza",
        height = 800,
    )
    html1 = fig.to_html()
    context = {'chart1': html1}
    return render(request, 'earthquakes/scatter1.html', context)
