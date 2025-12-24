from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="User")
    phone_number = models.CharField(max_length=15, blank=True,verbose_name="Phone")
    address = models.TextField(blank=True,verbose_name="Address")
    city = models.CharField(max_length=100, blank=True,verbose_name="City")
    state = models.CharField(max_length=100, blank=True,verbose_name="State")
    zip_code = models.CharField(max_length=10, blank=True,verbose_name="Zip Code")
    email_verified = models.BooleanField(default=False,verbose_name="Email Verfied")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.user.username

# Signal to create user profile when a new user is registered
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance,'userprofile'):
     instance.userprofile.save()