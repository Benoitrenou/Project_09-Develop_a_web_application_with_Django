from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
#from rules.contrib.models import RulesModelBase, RulesModelMixin
from PIL import Image


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    image = models.ImageField(null=True, blank=True, upload_to=settings.MEDIA_ROOT)
    time_created = models.DateTimeField(auto_now_add=True)
    has_review = models.BooleanField(default=False)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        if self.image:
            self.resize_image()
        super().save(*args, **kwargs)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )
    time_created = models.DateTimeField(auto_now_add=True)

    def save(self, ticket, user, *args, **kwargs):
        self.user = user
        self.ticket = ticket
        self.ticket.has_review = True
        self.ticket.save()
        super().save(*args, **kwargs)

class UserFollow(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
        )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
        )

    class Meta:
        unique_together = ('user', 'followed_user', )