from django.shortcuts import render

from .models import Slider
from .models import New
from .models import Page


# Create your views here.

# HomePage.
def homepage(request):
    slider = Slider.objects.all().order_by("order").filter(slider_online=True)
    context = {'slider': slider}
    return render(request, 'homepage.html', context)


def about(request):

    return render(request, 'about.html')


def news(request):
    news = New.objects.all().order_by("date")
    context = {
        'count': news.count(),
        'news': news
    }
    return render(request, 'news.html', context)

def new(request, slug):
    new = New.objects.get(slug=slug)
    context = {'new': new}
    return render(request, 'new.html',context)


def page(request, slug):
    page = Page.objects.filter(page_online=True).get(slug=slug)
    context = {'page': page}
    return render(request, 'page.html', context)

