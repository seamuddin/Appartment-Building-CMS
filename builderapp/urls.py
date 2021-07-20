from django.urls import path
from. import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('ongoing',views.ongoing, name='ongoing'),
    path('completed',views.completed, name='completed'),
    path('upcoming',views.upcoming, name='upcoming'),
    path('contactus',views.contactus, name='contactus'),
    path('testimonial',views.testimonial, name='testimonial'),
]
