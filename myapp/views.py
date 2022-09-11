from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from myapp.models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index</h1>")


def hello(request, username):
    return HttpResponse("<h2>Hola %s</h2>" % username)


def about(request):
    return HttpResponse("<h1>About</h1>")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request, id):
    task = Task.objects.get(id=id)
    return HttpResponse("task: %s" % task.name)
