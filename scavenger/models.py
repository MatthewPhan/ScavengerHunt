from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class Location(models.Model):

    location = models.CharField(max_length=100)
    code = models.ImageField(blank=True, upload_to='static/qrcodes')

    def save(self, *args, **kwargs):
        # Generate QR
        qr_image = qrcode.make(self.location) 
        qr_offset = Image.new('RGB', (310, 310), 'white')
        qr_offset.paste(qr_image)
        
        # Store QR
        files_name = f'{self.location}-qr.png' 
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

    # Tells Django Admin to print the instance of the location field of the model 
    def __str__(self):
        return self.location