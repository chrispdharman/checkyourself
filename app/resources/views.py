from django.http import HttpResponse
from django.template import loader

from .models import Resource


def index(request):
    urgent_resources = Resource.objects.order_by('-urgency_score')[:5]
    template = loader.get_template('resources/index.html')
    context = {
        'urgent_resources': urgent_resources,
    }
    return HttpResponse(template.render(context, request))
