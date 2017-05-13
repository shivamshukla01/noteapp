from django.shortcuts import render
from django.utils import timezone
from .models import Note, Subject, Branch

def index(request):
	"""
 	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	notes=Note.objects.all()
	branches=Branch.objects.all()
	subjects=Subject.objects.all()
	f=notes.filter(published_date__lte=timezone.now())
	notes=f.order_by('-created_date')[:4]

	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'notes':notes, 'branches':branches, 'subjects':subjects},
	)