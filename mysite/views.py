
# Django 
from django.http import HttpResponse

def my_custom_page_not_found_view(request, exception):
    import pudb; pudb.set_trace()
    return HttpResponse('Error handler 404', status=404)