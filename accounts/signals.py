from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    # this code add a new user to a customer group after the user is created
    if created:
        group = Group.objects.get(name='customer') # first of all get the group
        instance.groups.add(group) # adds the user the group

        # create a customer profile for a new user
        Customer.objects.create(
            user= instance,
            name= instance.username,
            email= instance.email
        )
        print('profile created')
