from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello world! I'm home.")

def about(request):
    return HttpResponse("My about page.")

def test(request):
    return HttpResponse("<h1><b>Hello</b></h1>")