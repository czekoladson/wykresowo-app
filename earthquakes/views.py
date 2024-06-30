from django.shortcuts import render
from earthquakes.models import PersonSalary
import plotly.express as px

def index(request):
    return render(request, 'earthquakes/index.html')

def info(request):
    return render(request, 'earthquakes/info.html')

def plot(request):
    person_salaries = PersonSalary.objects.all()
    ages = person_salaries.values_list('age', flat = True)
    salaries = person_salaries.values_list('salary', flat = True)
    fig = px.box(
        x = ages,
        y =salaries,
        title = "Salary By Age",
            height = 800)
    html = fig.to_html()
    context = {'chart': html}
    return render(request, 'earthquakes/scatter.html', context)
