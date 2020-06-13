from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# As this is the blogging webapllication we definately need the posts
# But For that we need a database to store the posts 
# So the below code is used to create to database for the posts

class Posts(models.Model):
    title=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    image=models.ImageField(default='defualt.jpg',upload_to='post_pics')
    video=models.FileField(upload_to='post_videos')
    video_enable=models.BooleanField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):

        return reverse('home:posts-detail', kwargs={"pk": self.pk})


# when a user uploads a image it automatically converts its resolution to the given resolution given below 
# It is used for efficient usage of storage
    def save(self ,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)
    