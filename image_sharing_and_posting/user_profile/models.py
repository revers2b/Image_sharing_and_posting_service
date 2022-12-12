from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
from django.template.defaultfilters import slugify
import os

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name="profile",
    )
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("User", self.username, instance)
        return None
    
    image = models.ImageField(default='default/user.jpg', upload_to=image_upload_to, max_length=255)
    
    def __str__(self) -> str:
        return f"{self.user} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            photo = Image.open(self.photo.path)
            if photo.width > 500 or photo.height > 500:
                output_size = (500, 500)
                photo.thumbnail(output_size)
                photo.save(self.photo.path)