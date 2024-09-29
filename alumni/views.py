
from django.http import HttpResponse
from django.template import loader
from .models import alumni_tb, dzolali, leased, books
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings
from django.http import Http404


# A NEW VIEW(FUNCTION) TO RETRIEVE ALL RECORDS FROM THE TABLE
def alumni_view(request):
  playoff_stars = dzolali.objects.all().values()
  template = loader.get_template('alumni_template.html')
  context = {
    'playoff_stars': playoff_stars,
  }
  return HttpResponse(template.render(context, request))

# A NEW VIEW(FUNCTION) TO RETRIEVE IDs
def details(request, id):
  playoff_stars = dzolali.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'playoff_stars': playoff_stars,
  }
  return HttpResponse(template.render(context, request))

# A NEW VIEW(FUNCTION) TO HANDLE THE DEFAULT PAGE
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
   
# A NEW VIEW(FUNCTION) TO TRY EXAMPLES
def items(request):
  nba = dzolali.objects.all()
  template = loader.get_template('templatez.html')
  context = {
    'nba_data': nba,
  }
  return HttpResponse(template.render(context, request))

# A NEW VIEW(FUNCTION) TO RETRIEVE ALL RECORDS FROM THE LEASED TABLE
def leased_view(request):
  leasings = leased.objects.all().values()
  template = loader.get_template('leased_items.html')
  context = {
    'leasings': leasings,
  }
  return HttpResponse(template.render(context, request))


# A NEW VIEW(FUNCTION) TO HANDLE LEASED DETAILS
def leased_details(request, id):
  leaser = leased.objects.get(id=id)
  template = loader.get_template('leased_details.html')
  context = {
    'leaser': leaser,
  }
  return HttpResponse(template.render(context, request))

# A NEW VIEW(FUNCTION) TO REDIRECT TO EXTERNAL LINK(LEARNERSPLATFORM.COM)
#def my_redirect(request):
 # return redirect("https://account.learnersplatform.com/login")


# A NEW VIEW(FUNCTION) TO RETRIEVE ALL BOOKS FROM THE BOOKS TABLE
def book_view(request):
  library = books.objects.all().values()
  template = loader.get_template('book.html')
  context = {
    'library': library,
  }
  return HttpResponse(template.render(context, request))

# A NEW VIEW(FUNCTION) TO HANDLE BOOK DETAILS
def book_details(request, id):
  kamil = books.objects.get(id=id)
  template = loader.get_template('book_details.html')
  context = {
    'kamil': kamil,
  }
  return HttpResponse(template.render(context, request))

  
# A NEW VIEW(FUNCTION) TO HANDLE NAVIGATION SCHEME
def my_navigation(request):
    # Logic for your view
    context = {}
    referer = request.META.get('HTTP_REFERER')
    if referer:
        context['referer'] = referer
    return render(request, 'details.html', context)


# A NEW VIEW(FUNCTION) TO DISPLAY SIMPLE HTML PAGE CALLED KAMIL.HTML
def extra(request):
    return render(request, 'kamil.html')

# A NEW VIEW(FUNCTION) TO DISPLAY PDF ON BUTTON CLICK
def pdf_view(request):
    filepath = os.path.join(settings.STATIC_ROOT, 'kana', 'alumni', 'static', 'RENEWAL.pdf')
    if os.path.exists(filepath):
        with open(filepath, 'rb') as pdf:
            response = FileResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="RENEWAL.pdf"'
            return response
    else:
        # Handle the error: file not found
        from django.http import Http404
        raise Http404("PDF file not found.")
   
  

    














