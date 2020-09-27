from django.shortcuts import render,redirect
from .forms import FeedbackForm
from django.contrib import messages

def contact_view(request):

    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'İsteğiniz başarılı bir şekilde alınmıştır.')
        return redirect('contact')


    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)