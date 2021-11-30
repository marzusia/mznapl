from django.shortcuts import render


def handler404(request, exception=None):
    return render(request, 'mznapl/error/404.jinja')


def handler500(request, exception=None):
    return render(request, 'mznapl/error/500.jinja')
