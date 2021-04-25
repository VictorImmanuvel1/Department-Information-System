from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Education,oe,ap,article,seminar,student,sem1,sem2,sem3,sem4,sem5

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        Education.objects.create(user=instance)
        oe.objects.create(user=instance)
        ap.objects.create(user=instance)
        article.objects.create(user=instance)
        seminar.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    instance.profile.save()
    instance.education.save()
    instance.oe.save()
    instance.ap.save()
    instance.article.save()
    instance.seminar.save()

@receiver(post_save,sender=student)
def create(sender,instance,created,**kwargs):
    if created:
        sem1.objects.create(sid=instance)
        sem2.objects.create(sid=instance)
        sem3.objects.create(sid=instance)
        sem4.objects.create(sid=instance)
        sem5.objects.create(sid=instance)


@receiver(post_save,sender=student)
def save(sender,instance,created,**kwargs):
    instance.sem1.save()
    instance.sem2.save()
    instance.sem3.save()
    instance.sem4.save()
    instance.sem5.save()