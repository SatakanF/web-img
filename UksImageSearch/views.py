from django.shortcuts import render
from django.views.generic.base import View
from .models import Product,Logo
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.

class Home(View):

    def get(self,requests):
        products = Product.objects.all()
        logos = Logo.objects.all()
        return render(requests,'UksImageSearch/base.html',{'products':products,'logos': logos})



class SearchA(ListView):
    model  = Product
    template_name = 'UksImageSearch/search.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(article__icontains=query)
        )
        return object_list

class SearchC(ListView):
    model  = Product
    template_name = 'UksImageSearch/searchC.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('c')
        object_list = Product.objects.filter(
            Q(product_code__icontains=query)
        )
        return object_list
