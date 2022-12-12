from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
import os
from django.template.defaultfilters import slugify

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name="profile",
    )
    
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None
    image = models.ImageField("photo", upload_to='user_profile/photos', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            photo = Image.open(self.image.path)
            if photo.width > 500 or photo.height > 500:
                output_size = (500, 500)
                photo.thumbnail(output_size)
                photo.save(self.image.path)