from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from django.utils import timezone
import os

User = get_user_model()


class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True) 
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    article_slug = models.SlugField("Article slug", null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default="")
    notes = HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']


# class Like(models.Model):
#     upload = models.ForeignKey(
#         ArticleSeries,
#         verbose_name=("upload"),
#         on_delete=models.CASCADE,
#         related_name="Like"
#     )
#     user = models.ForeignKey(
#         User, verbose_name=("User"),
#         on_delete=models.CASCADE,
#         related_name="Upload_like",
#     )

#     def __str__(self) -> str:
#         return f"{self.user} likes {self.upload}"


# class comment(models.Model):
#     upload = models.ForeignKey(
#         ArticleSeries,
#         verbose_name=("upload"),
#         on_delete=models.CASCADE,
#         related_name="Comments",
#     )
#     body = models.TextField(("comment"), max_length=200)
#     user = models.ForeignKey(
#         User,
#         verbose_name=("User"),
#         on_delete=models.CASCADE,
#         related_name="comments"
#     )

#     def __str__(self) -> str:
#         return ("Commented on {upload_id}, by {user}").format(
#             upload_id=self.upload.id,
#             user=self.user,
#         )