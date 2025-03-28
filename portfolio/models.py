from django.db import models
from rembg import remove
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=20)
    another_phone= models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(max_length=800,null=True,blank=True)
    
    def __self__(self):
        return(self.name)
    
class myPersonalInfo(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100,null=True,blank=True)
    facebook = models.CharField(max_length=100,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)
    linkedin = models.CharField(max_length=100,null=True,blank=True)
    github = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    another_phone= models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(max_length=800,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    skills = models.TextField(max_length=800,null=True,blank=True)
    education = models.TextField(max_length=800,null=True,blank=True)
    
    
    def save(self, *args, **kwargs):
        # Process the image only if it exists and hasn’t been processed yet
        if self.image and not self.image.name.startswith('processed_'):
            # Open the original image
            input_image = Image.open(self.image)
            # Remove the background
            output_image = remove(input_image)
            # Save to a bytes buffer
            buffer = BytesIO()
            output_image.save(buffer, format='PNG')
            buffer.seek(0)
            # Create a new file name
            original_name = self.image.name
            new_name = 'processed_' + original_name
            # Update the image field with the processed image
            self.image.save(new_name, ContentFile(buffer.getvalue()), save=False)
        # Call the parent save method
        super().save(*args, **kwargs)
        
    def __self__(self):
        return(self.name)