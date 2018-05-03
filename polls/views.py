from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Ici on parle français")
