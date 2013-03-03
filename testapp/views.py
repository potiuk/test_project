# Create your views here.
from django.http import HttpResponse


def view(request):
    return HttpResponse("All OK")