from django.http import Http404 , HttpResponse  
import datetime
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render



def date_time(request):
	now = datetime.datetime.now()
	##t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date' : now}))
	
	#return HttpResponse(html)
	
	#using render fucntion
	return render (request, 'practice\current_datetime.html', {'current_date' : now})
	

def hello(request):
    return HttpResponse("Hello world")
	

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))



	
#def search(request):
  #  if 'q' in request.GET:
  #      message = 'You searched for: %r' % request.GET['q']
  #  else:
 #       message = 'You submitted an empty form.'
 #   return HttpResponse(message)
 
 
 
 
	

