from django.db import models
from .utils import get_merged_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

class Upload(models.Model):
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images',null=True)
    
    def __str__(self):
        return str(self.pk)
    
    def save(self, *args, **kwargs):
        #open image
        pil_img1 = Image.open(self.image1)
        pil_img2 = Image.open(self.image2)
        
        #convert image to array
        cv_image1 = np.array(pil_img1)
        cv_image2 = np.array(pil_img2)
        img = get_merged_image(cv_image1, cv_image2)
        
        #convert back to pil image
        im_pil = Image.fromarray(img)
        
        #save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()
        
        self.image1.save(str(self.image1), ContentFile(image_png), save=False)
        super().save(*args, **kwargs)
