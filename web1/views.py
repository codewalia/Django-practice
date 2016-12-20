from django.shortcuts import render
from web1.models import Book
# Create your views here.

#def search_form(request):
  #  return render(request, 'search_form.html')


#def search(request):
  #  if 'q' in request.GET and request.GET['q']:
    #    q = request.GET['q']
   #     books = Book.objects.filter(title__icontains=q)
   #     return render(request, 'search_results.html',
   #                   {'books': books, 'query': q})
   # else:
   #     #return HttpResponse('Please submit a search term.')
	#	return render(request, 'search_form.html', {'error': True})



def search(request):
	error = False
	if 'q' in request.GET:
		q=request.GET['q']
		if not q:
			error = True
		elif len(q) > 20:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html',{'books': books, 'query' :q})
	return render(request, 'search_form.html', {'error':error})
