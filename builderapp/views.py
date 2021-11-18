from django.shortcuts import render

# Create your views here.
from builderapp.forms import ContactForm
from django.shortcuts import redirect
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def ongoing(request):
    return render(request, 'ongoing_project.html')

def upcoming(request):
    return render(request, 'upcoming_project.html')

def completed(request):
    return render(request, 'completed_project.html')


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thank You for contacting us. We will get back to you shortly!')
            return redirect('/contactus/')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contactus.html')

def testimonial(request):
    return render(request, 'testimonial.html')


def details(request):
    return render(request, 'details.html')