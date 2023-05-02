from django.db import models
import qrcode
from datetime import datetime
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Location(models.Model):

    # location_name field (stores the location name)
    location_name = models.CharField(max_length=100, unique=True)

    qrcode_filepath = models.ImageField(blank=True, upload_to='qrcodes')

    location_description = models.CharField(max_length=10000, unique=True)

    location_fun_fact = models.CharField(max_length=1000, unique=True, blank=True, null=True)

    location_image = models.ImageField(upload_to='locations/', default='../media/locations/default.jpg')

    location_badge = models.ImageField(upload_to='badges/', default='../media/locations/default.jpg')

    # Print the instance of the location_name field of the model
    def __str__(self):
        
        # To return location variables 
        return '{} {} {} {} {}'.format(self.location_name, self.location_description, self.location_image, self.location_fun_fact, self.location_badge)
    
    # save() function to generate QR Code based on location name
    def save(self, *args, **kwargs):

        # Append the substring "NUSSOCSH23", which serves as an identifier for validation of QR Codes generated by our Web App
        qrcode_data = f'{self.location_name}NUSSOCSH23'

        # Generate QR Code
        qrcode_image = qrcode.make(qrcode_data)
        canvas = Image.new('RGB', (qrcode_image.pixel_size, qrcode_image.pixel_size), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image)
        
        # Store QR Code based on location name
        fname = f'{self.location_name}-qr_code.png'
        stream = BytesIO()
        canvas.save(stream, 'PNG')
        self.qrcode_filepath.save(fname, File(stream), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Event(models.Model):
    name = models.CharField(max_length=200)
    when = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        # To return event variables 
        return '{} {}'.format(self.name, self.when)