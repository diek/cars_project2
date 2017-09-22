from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.functional import cached_property


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    @cached_property
    def contact_data(self):
        """Get related secondary contact information"""
        return self.secondaryemailsms_set.order_by('id')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class SecondaryEmailSMS(models.Model):
    users = models.ManyToManyField(User)
    alternate_email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    alternate_sms_telephone = models.CharField(verbose_name='telephone', max_length=20, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.alternate_email, self.alternate_sms_telephone)
