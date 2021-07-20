from django.shortcuts import render

# Create your views here.

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
    return render(request, 'contactus.html')

def testimonial(request):
    return render(request, 'testimonial.html')