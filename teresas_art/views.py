from django.shortcuts import render


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template



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

def contact(request):
	form_class = ContactForm

	# email logic
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
			template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
				})
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"Teresa Derdiarian Art" +'',
				['teresaderdiarian@gmail.com'],
				headers = {'Reply-To': contact_email }
            )

			email.send()
			return redirect('/recent/')

	return render(request, 'contact.html', {'form': form_class, })