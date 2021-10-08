from django.db import models

# Create your models here.


class GeneralSettings(models.Model):
    logo = models.ImageField(upload_to='uploads/logo/')
    title = models.CharField(max_length=512, verbose_name='Title', blank=True, null=True)
    mobile_no = models.CharField(blank=False, null=False, max_length=20, verbose_name='Contact No (Mobile')
    phone_no = models.CharField(blank=True, null=True, max_length=20, verbose_name='Contact No (Phone)')
    facebook_link = models.CharField(blank=True, null=True, max_length=512, verbose_name='Facebook Link')
    youtube_link = models.CharField(blank=True, null=True, max_length=512, verbose_name='Youtube Link')
    instagram_link = models.CharField(blank=True, null=True, max_length=512, verbose_name='Instagram Link')
    linkedin_link = models.CharField(blank=True, null=True, max_length=512, verbose_name='Linkedin Link')
    twitter_link = models.CharField(blank=True, null=True, max_length=512, verbose_name='Twitter Link')
    footer = models.CharField(blank=True, null=True, max_length=1024, verbose_name='Footer')
    about_us = models.TextField(blank=True, null=True, max_length=4096, verbose_name='About Us')
    contact_us = models.TextField(blank=True, null=True, max_length=4096, verbose_name='Contact Us')

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=256, blank=False)
    code = models.CharField(max_length=10, blank=False)
    start_date = models.DateField(default=None, blank=True)
    tentative_end_date = models.DateField(default=None, blank=True)
    project_value = models.DecimalField(max_length=15, max_digits=15, decimal_places=6)


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='uploads/project/')
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
