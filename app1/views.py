from django.http import HttpResponse
from django.template import loader
from .models import Member
def app1(request):
    template = loader.get_template('index.html')
    
    mymembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))