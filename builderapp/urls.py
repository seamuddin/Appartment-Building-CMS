from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from. import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('ongoing', views.ongoing, name='ongoing'),
    path('completed', views.completed, name='completed'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('contactus', views.contactus, name='contactus'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('details_view', views.details, name='details'),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
