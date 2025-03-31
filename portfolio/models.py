from io import BytesIO
from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader
from PIL import Image
from rembg import remove 

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
    name = models.CharField(max_length=80,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    facebook = models.CharField(max_length=100,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)
    linkedin = models.CharField(max_length=100,null=True,blank=True)
    github = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    another_phone= models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(max_length=800,null=True,blank=True)
    image = CloudinaryField('image')
    skills = models.CharField(max_length=800,null=True,blank=True)
    education = models.TextField(max_length=800,null=True,blank=True)
    job =models.CharField(max_length=200,null=True,blank=True)
    hits = models.IntegerField(default=0)
    
    
    def save(self, *args, **kwargs):
        # Process the image only if it exists and its name doesn't already start with 'processed_'
        if self.image and not self.image.name.startswith('processed_'):
            try:
                # Open the original image using Pillow
                input_image = Image.open(self.image)
            except Exception as e:
                print("Error opening image:", e)
                return super().save(*args, **kwargs)
            
            # Remove the background (using rembg)
            output_image = remove(input_image)
            
            # Save the processed image to an in-memory bytes buffer in PNG format
            buffer = BytesIO()
            output_image.save(buffer, format='PNG')
            buffer.seek(0)
            
            # Generate a new public_id for the processed image.
            # Here we strip the extension from the original name.
            original_name = self.image.name
            base_name = original_name.rsplit('.', 1)[0]
            new_public_id = 'processed_' + base_name
            
            # Upload the processed image to Cloudinary.
            # Optionally, you can specify a folder by adding folder='your_folder' in the arguments.
            upload_result = cloudinary.uploader.upload(
                buffer,
                public_id=new_public_id
            )
            # Set the image field to the new public_id.
            self.image = upload_result['public_id']
            
        # Call the parent save method to store the model instance.
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    
class portfolio(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=800,null=True,blank=True)
    image = CloudinaryField('image/portfolio')
    link = models.CharField(max_length=100,null=True,blank=True)
    
    def __self__(self):
        return(self.title)
    
