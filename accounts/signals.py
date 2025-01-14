from gettext import install
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from .models import Profile, Teacher, Student

User = get_user_model()
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
            print('instance' , instance)
            print('email', instance.email)
            
            Student.objects.create(user=instance, email=instance.email)
        elif instance.is_teacher:
            Teacher.objects.create(user=instance, email=instance.email)
        else:
            Profile.objects.create(user=instance, email=instance.email)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

