from io import BytesIO
from django.db import models
# from cloudinary.models import CloudinaryField
# import cloudinary.uploader
from PIL import Image
from rembg import remove 
from django.urls import reverse
from django.utils import timezone

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
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    # image = CloudinaryField('image')
    skills = models.CharField(max_length=800,null=True,blank=True)
    education = models.TextField(max_length=800,null=True,blank=True)
    job =models.CharField(max_length=200,null=True,blank=True)
    hits = models.IntegerField(default=0)
    
    
    # def save(self, *args, **kwargs):
    #     # Only process if an image is provided and this is a new upload.
    #     # We attempt to get a name attribute; if not available, we assume it's already processed.
    #     original_name = getattr(self.image, 'name', '')
    #     if self.image and original_name and not original_name.startswith('processed_'):
    #         try:
    #             # Open the original image with Pillow
    #             input_image = Image.open(self.image)
    #         except Exception as e:
    #             print("Error opening image:", e)
    #             return super().save(*args, **kwargs)
            
    #         # Remove the background using rembg
    #         output_image = remove(input_image)
            
    #         # Save the processed image to an in-memory buffer in PNG format
    #         buffer = BytesIO()
    #         output_image.save(buffer, format='PNG')
    #         buffer.seek(0)
            
    #         # Generate a new public_id for the processed image.
    #         base_name = original_name.rsplit('.', 1)[0]
    #         new_public_id = 'processed_' + base_name
            
    #         # Upload the processed image to Cloudinary.
    #         upload_result = cloudinary.uploader.upload(
    #             buffer,
    #             public_id=new_public_id
    #         )
    #         # Set the image field to the new public_id (CloudinaryField expects a public ID)
    #         self.image = upload_result['public_id']
        
    #     # Call the parent save method
    #     super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        # Only process if an image is provided and this is a new upload.
        original_name = getattr(self.image, 'name', '')
        if self.image and original_name and not original_name.startswith('processed_'):
            try:
                # Open the original image with Pillow
                input_image = Image.open(self.image)
            except Exception as e:
                print("Error opening image:", e)
                return super().save(*args, **kwargs)
            
            # Remove the background using rembg
            output_image = remove(input_image)
            
            # Save the processed image to an in-memory buffer in PNG format
            buffer = BytesIO()
            output_image.save(buffer, format='PNG')
            buffer.seek(0)
            
            # Generate a new file name for the processed image
            base_name = original_name.rsplit('.', 1)[0]
            new_file_name = f'processed_{base_name}.png'
            
            # Save the processed image locally
            self.image.save(new_file_name, buffer, save=False)
        
        # Call the parent save method
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    
    
class portfolio(models.Model):
    title = models.CharField(max_length=80)
    # slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=800,null=True,blank=True)
    # image = CloudinaryField('image/portfolio')
    image = models.ImageField(upload_to='images/portfolio/',null=True,blank=True)
    link = models.CharField(max_length=100,null=True,blank=True)
    publish = models.DateTimeField(default=timezone.now)
    
    # class Meta:
    #     ordering =['-publish']
    #     indexes = [
    #         models.Index(fields=['-publish'])
    # ]
    
    def __str__(self):
        return self.title
    
    
    # def get_absolute_url(self):
    #     return reverse("portfolio",args=[
    #         self.publish.year,
    #         self.publish.month,
    #         self.publish.day,
    #         self.slug,
    #         ])
    
