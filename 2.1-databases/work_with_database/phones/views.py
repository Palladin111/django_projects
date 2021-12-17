from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()

    context = {
       'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_all = Phone.objects.all()
    for phone in phone_all:
        if phone.slug == slug:
           context = {
                'phone': phone
            }
           return render(request, template, context)

