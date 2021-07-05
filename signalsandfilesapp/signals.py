from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Details


# the token is generated after the model is saved
@receiver(post_save, sender=User)
def generate_token(sender, instance, created, **kwargs):
    if created:
        print(instance)
        user = User.objects.get(username=instance)
        user_id = user.pk
        token_gen = Token.objects.create(user_id=user_id)
        token_gen.save()
        generatedtoken = Token.objects.get(user=user_id)
        key = generatedtoken.key
        print(key)


'''
We need to Configure the signals in apps.py
'''

'''Signals are used to perform any action on modification of a model instance. 
The signals are utilities that help us to connect events with actions. 
We can develop a function that will run when a signal calls it. 
In other words, Signals are used to perform some action on modification/creation of a particular entry in Database. 
For example, One would want to create a profile instance, as soon as a new user instance is created in Database

There are 3 types of signal.

pre_save: This signal  works before  the  method save() in model.
post_save : This signal  works after  the  method save() in model.
pre_delete/post_delete: This signal  works before after delete a model’s instance (method delete()) this signal is thrown.
pre_init/post_init: This signal is thrown before/after instantiating a model (__init__() method).
'''
