from django.shortcuts import render


def index(request):
    template = 'core/home/main.html'
    context = {}
    return render(request, template, context)
