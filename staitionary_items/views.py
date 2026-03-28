from django.shortcuts import render

def all_item(request):
    return render(request, 'index.html')