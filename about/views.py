from django.shortcuts import render,get_object_or_404
from .models import About


def about_view(request):
    about =get_object_or_404(About)

    context = {
        'about': about,
    }


    return render(request, 'about.html', context)