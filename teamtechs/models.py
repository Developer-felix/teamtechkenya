from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust,ResizeToFit
from pilkit.processors import Thumbnail

#models
#about
#team
#home


#general choices  page models
pages = [
    ('About','about-our-teamtechkenya-company'),
     ('Services','services'),
      ('Portofolio','portofolio'),
       ('Team','teamtechkenya-partners'),
]


#home
class LandingPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='home')
    image = ImageSpecField(processors=[ResizeToFill(1920, 1280)], source='img',
            format='PNG', options={'quality': 100})
    
    class Meta:
        verbose_name_plural = "LandingPage"
    
    def __str__(self):
        return self.title

#about 
class About(models.Model):
    slug = models.SlugField(max_length=15,choices=pages)
    img = models.ImageField(upload_to='about')
    image = ImageSpecField(processors=[ResizeToFill(800, 496)], source='img',
            format='PNG', options={'quality': 100})
    
    class Meta:
        verbose_name_plural = "About"
    



#team
class Team(models.Model):
    slug = models.SlugField(max_length=15,choices=pages)
    partner = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    img = models.ImageField(upload_to='team-members')
    image = ImageSpecField(processors=[ResizeToFill(400, 400)], source='img',
            format='PNG', options={'quality': 100})
    
    class Meta:
        verbose_name_plural = "Team"
    
    def __str__(self):
        return f'{self.partner}  {self.position}'


#Services
class Services(models.Model):
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.service_name

#Contact
class Contact(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = "Contact"
    
    def __str__(self):
        return self.email

#Projects
class Projects_web(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='projects-done')
    image = ImageSpecField(processors=[ResizeToFill(800, 600)], source='img',
            format='PNG', options={'quality': 100})
    
    class Meta:
        verbose_name_plural = "Projects_web"
    
    def __str__(self):
        return self.name

class Projects_loan(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='projects-done')
    image = ImageSpecField(processors=[ResizeToFill(800, 600)], source='img',
            format='PNG', options={'quality': 100})
    
    class Meta:
        verbose_name_plural = "Projects_loan"
    
    def __str__(self):
        return self.name


class Projects_webstartup(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='projects-done')
    image = ImageSpecField(processors=[ResizeToFill(800, 600)], source='img',
            format='PNG', options={'quality': 100})
    
    class Meta:
        verbose_name_plural = "Projects_webstartup"
    
    def __str__(self):
        return self.name
