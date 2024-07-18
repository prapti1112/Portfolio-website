import json
from django.http import Http404
from django.shortcuts import render
from .models import Skill, WorkExperience


with open("color_palette.json") as file:
    color_pallete = json.load(file)


def index(request):
    try:
        skills = Skill.objects.all()
    except Skill.DoesNotExist:
        raise Http404("No skills found!")
    
    try:
        work_experience = WorkExperience.objects.all().order_by('-start_date', '-end_date')
    except WorkExperience.DoesNotExist:
        raise Http404("No workexperience found!")
    projects, blogs = list(range(12)), list(range(12))

    return render(request, 'portfolio/home.html', {**color_pallete, "font-style": "Open Sans", "skills": skills, "work_experience": work_experience, "projects": projects, "blogs": blogs})