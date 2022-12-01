from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Upload(models.Model):
    title = models.CharField(("Title"), max_length=100)
    description = models.TextField(("Description"), max_length=20000)
    user = models.ForeignKey(
        User,
        verbose_name=("user"),
        on_delete=models.CASCADE,
        related_name="posts",
    )
    image = models.ImageField(("image"), upload_to="user_images/", blank=True, null=True)

    def __str__(self) -> str:
        return ("{title} by {user}").format(title=self.title, user=self.user)
