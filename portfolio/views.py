from django.shortcuts import render
from .models import Project,Resume


def home(request):
    projects = Project.objects.all()
    resumes = Resume.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects,
                                                   'resumes': resumes
                                                   })

