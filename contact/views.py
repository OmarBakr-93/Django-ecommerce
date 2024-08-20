from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import Contact_form, Subscriber_form


# Create your views here.
def contact_page(request):
    form = Contact_form()
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Submitted.')
            return redirect('contact')
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)

def base_page(request):
    forms = Subscriber_form()
    if request.method == 'POST':
        forms = Subscriber_form(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms
    }
    return render(request, 'home.html', context)