from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>Welcome to staionery management system by aditya </h1>")

def about(request):
  return HttpResponse("<h1>staionery mangement system</h1>")

def contact(request):
  return HttpResponse("<h1>printing system</h1>")