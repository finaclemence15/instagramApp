from django.test import TestCase
from . models import Image, Profile, Comments

# Create your tests here.

class ImageTestClass(TestCase):
            # Set up method
    def setUp(self):
        self.butterfly= Image(image = 'book.jpg', name ='butterfly', caption ='about butterfly')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.butterfly,Image))        
        
        # Testing Save Method of Image model
    def test_save_method(self):
        self.butterfly.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)        