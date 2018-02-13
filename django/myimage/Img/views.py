from django.shortcuts import render
from .form import ImgForm
from django.shortcuts import render_to_response
from .models import Img
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImgForm()
    return render_to_response('add.html', {'form': form})


def list(request):
    template_var={}
    photos=Img.objects.all()
    template_var['pics']=photos
    return render_to_response('list.html',template_var,
                       context_instance=RequestContext(request))