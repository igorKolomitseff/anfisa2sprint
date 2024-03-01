from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    return render(request, 'homepage/index.html', {
        'ice_cream_list': IceCream.objects.values(
            'id', 'title', 'price', 'description'
        ).filter(
            is_published=True,
            is_on_main=True,
            category__is_published=True
        )
    })
