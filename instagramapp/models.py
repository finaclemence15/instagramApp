from django.db import models

# Create your models here.
        
class Profile(models.Model):
    profile = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =60)
    
    def __str__(self):
        return self.bio

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return instagramapp    
    
class Image (models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =40)
    caption= models.CharField(max_length =60)
    likes = models.IntegerField(default='none')
    comments= models.CharField(max_length =100)
    profile = models.ForeignKey(Profile,null = True)

    def __str__(self):
        return self.name
    
class Meta:
        ordering = ['name']        
        