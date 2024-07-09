import json
from venv import logger
# from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
# from portfolio.models import Category
from projects.models import Project
from .filters import ProjectFilter
from django.views.decorators.csrf import requires_csrf_token
from django.core.files.storage import FileSystemStorage


with open("color_palette.json") as file:
    color_pallete = json.load(file)

class ProjectsListView(ListView):
    """View to show different projects

    Args:
        ListView (django.views.generic.ListView): .

    Returns:
        context: context for the view
    """
    model = Project
    template_name = r"projects\project_card_view.html"
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["projects"] = Project.objects.all()
        # context["categories"] = Category.objects.all()
        context['form'] = self.filterset.form

        context = { **context, **color_pallete}

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProjectFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

class ProjectDetailView(DetailView):
    """Deatils view showing each project.

    Args:
        DetailView (django.views.generic.DetailView): .
    """
    model = Project
    template_name = r"projects\project_detail_view.html"
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = { **context, **color_pallete}
        return context


@requires_csrf_token
def upload_image(request):
    f=request.FILES['image']
    fs=FileSystemStorage()
    filename=str(f).split('.')[0]
    file= fs.save(filename,f)
    fileurl=fs.url(file)
    return JsonResponse({'success':1,'file':{'url':fileurl}})

@requires_csrf_token
def upload_file(request):
        f=request.FILES['file']
        fs=FileSystemStorage()
        filename,ext=str(f).split('.')
        print(filename,ext)
        file=fs.save(str(f),f)
        fileurl=fs.url(file)
        fileSize=fs.size(file)
        return JsonResponse({'success':1,'file':{'url':fileurl,'name':str(f),'size':fileSize}})


def upload_link_view(request):
    import requests
    from bs4 import BeautifulSoup  

    print(request.GET['url'])
    url = request.GET['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text,features="html.parser")
    metas = soup.find_all('meta')
    description=""
    title=""
    image=""
    for meta in metas:
        if 'property' in meta.attrs:
            if (meta.attrs['property']=='og:image'):
                image=meta.attrs['content']         
        elif 'name' in meta.attrs:         
            if (meta.attrs['name']=='description'):
                description=meta.attrs['content']
            if (meta.attrs['name']=='title'):
                title=meta.attrs['content']
    return JsonResponse({'success':1,'meta':
    {"description":description,"title":title, "image":{"url":image}}
})