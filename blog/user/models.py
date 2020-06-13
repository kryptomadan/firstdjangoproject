from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#Database for the Userprofile Details
class Profile(models.Model):
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}profile'
    
    def save(self ,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)


