from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Ini adalah halaman dashboard")