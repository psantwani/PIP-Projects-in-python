from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.views import generic

#python -m pip install matplotlib
from matplotlib import font_manager

def index(request):
	template = loader.get_template('fonts/index.html')
	fontList = [f.name for f in font_manager.fontManager.ttflist]
	fontSet = set(fontList)
	context = {
        'fontList': list(fontSet),
    }
	return HttpResponse(template.render(context, request))