from .models import Standard

def standard_list(request):
    standard_list = Standard.objects.all()
    kwargs = {
        'standard_list':standard_list
    }
    return kwargs