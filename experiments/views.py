import json
from .models import Experiment
from experiments.filters import ExperimentFilter
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import requires_csrf_token


with open("color_palette.json") as file:
    color_pallete = json.load(file)


class ExperimentsListView(ListView):
    """View to show different experiments

    Args:
        ListView (django.views.generic.ListView): .

    Returns:
        context: context for the view
    """
    model = Experiment
    template_name = r"experiments\experiment_card_view.html"
    context_object_name = 'experiments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form

        context = { **context, **color_pallete}

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ExperimentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

class ExperimentDetailView(DetailView):
    """Deatils view showing each experiment.

    Args:
        DetailView (django.views.generic.DetailView): .
    """
    model = Experiment
    template_name = r"experiments\experiment_detail_view.html"
    context_object_name = 'experiment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = { **context, **color_pallete}
        return context


@requires_csrf_token
def upload_image(request):
    f = request.FILES.get('image', None)
    if not f:
        return JsonResponse({'success':0,'file':{'url': "Unable to save file"}})
    
    print( f"File_path: {f}" )
    fs=FileSystemStorage()
    print( f"Saving file to: /media/uploads/experiments/contents/images/{f}" )
    file= fs.save(fr"uploads/experiments/contents/images/{f}", f)
    fileurl=fs.url(file)
    return JsonResponse({'success':1,'file':{'url':fileurl}})

@requires_csrf_token
def upload_file(request):
        f=request.FILES.get('file', None)
        if not f:
            return JsonResponse({ 'success':0,'file':"Unable to save file" })

        fs=FileSystemStorage()
        filename, ext=str(f).split('.')
        print(filename,ext)
        file=fs.save(f"uploads/experiments/contents/files/{f}",f)
        fileurl=fs.url(file)
        fileSize=fs.size(file)
        return JsonResponse({'success':1,'file':{'url':fileurl,'name':str(f),'size':fileSize}})


def upload_link_view(request):
    import requests
    from bs4 import BeautifulSoup  

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