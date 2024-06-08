from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from myauth.models import News

class Index(ListView):
    template_name = 'appearance/index.html'
    model = News
    context_object_name = "news"

class NewsView(ListView):
    template_name = 'appearance/news_list.html'
    model = News
    context_object_name = "news"

class NewsDetailsView(View):
    def get(self, request:HttpRequest, pk: int) -> HttpResponse:
        new = get_object_or_404(News,pk=pk)
        context = {
            "new": new,
        }
        return render(request, 'appearance/news_details.html', context=context)

class AboutUs(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'appearance/about_us.html')

class Contact(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'appearance/contact.html')