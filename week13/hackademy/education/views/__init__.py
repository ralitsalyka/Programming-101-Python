from django.shortcuts import render

# import education.views.courses


def index(request):
    return render(request, 'index.html', {})
