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
    image = models.ImageField(("image"), upload_to="images/", blank=True, null=True)

    def __str__(self) -> str:
        return ("{title} by {user}").format(title=self.title, user=self.user)


class Like(models.Model):
    upload = models.ForeignKey(
        Upload,
        verbose_name=("upload"),
        on_delete=models.CASCADE,
        related_name="Like"
    )
    user = models.ForeignKey(
        User, verbose_name=("User"),
        on_delete=models.CASCADE,
        related_name="Upload_like",
    )

    def __str__(self) -> str:
        return f"{self.user} likes {self.upload}"