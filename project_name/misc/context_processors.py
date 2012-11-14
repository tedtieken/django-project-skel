from django.conf import settings

def date_formats(request):
    return {
        'date_format_long': 'l j F Y',
    }
    
def is_local(request):
  return {'IS_LOCAL': settings.IS_LOCAL}
    