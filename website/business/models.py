from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here:
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    #Here, we allow the account balance to never exceed 1 million.
    accountBalance = models.DecimalField(max_digits=9, decimal_places=2, default = 0.00)
    isVIP = models.BooleanField(default=False)

    def checkForVIP(self):
        if accountBalance > 5,000.00:
            isVIP = true


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



    def __str__(self):
        return self.text
