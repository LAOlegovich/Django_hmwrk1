from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    data = Phone.objects.all()
    par = request.GET.get("sort","name")
    match par:
        case "name": f = False
        case "min_price":f = False
        case "max_price": f = True
    data_sorted= sorted(list(data), key = lambda x:x.get_p(par),reverse = f)
    context = {'phones':data_sorted}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    data = Phone.objects.get(slug = slug)
    context = {'phone':data}
    return render(request, template, context)
