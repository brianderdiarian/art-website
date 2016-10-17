from django.shortcuts import render


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response



from random import randint
# Create your views here.

from .models import Artwork, Info

def index(request):
# Create your views here.
	artworks = Artwork.objects.order_by('-uploaded')[:1]
	context = {'artworks': artworks}
	return render(request, 'index.html', context)

def recent(request):
# Create your views here.
	artworks = Artwork.objects.order_by('-uploaded')
	context = {'artworks': artworks}
	return render(request, 'recent.html', context)

def works(request):
# Create your views here.
	artworks_2016 = Artwork.objects.filter(year__year_made__contains=2016)
	artworks_2015 = Artwork.objects.filter(year__year_made__contains=2015)
	artworks_2014 = Artwork.objects.filter(year__year_made__contains=2014)
	earlier = Artwork.objects.filter(year__year_made__lte=2014)
	
	context = {
		'artworks_2016': artworks_2016,
		'artworks_2015': artworks_2015,
		'artworks_2014': artworks_2014,
		'earlier': earlier,
	}
	return render(request, 'works.html', context)

def cv(request):
# Create your views here.
	infos = Info.objects.all
	context = {'infos': infos}
	return render(request, 'cv.html', context)

def about(request):
# Create your views here.
	infos = Info.objects.all
	context = {'infos': infos}
	return render(request, 'about.html', context)