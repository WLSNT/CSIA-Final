import datetime
from tkinter import CASCADE

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tag(models.Model):
    tag_text = models.TextField(default='', blank=True)
    
    def set_tag_text(self, new_text):
        self.tag_text = new_text
        self.save()
        return self.tag_text

    def __str__(self):
        return self.tag_text

class Folder(models.Model): #folder object
    folder_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.datetime.now(), editable=True)
    is_important = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)

    def set_tags(self, new_tags):
        self.tags = new_tags
        self.save()
        return self.tags

    def set_creator(self, new_creator):
        self.creator = new_creator
        self.save()
        return self.creator

    def set_folder_text(self, new_text):
        self.folder_text = new_text
        self.save()
        return self.folder_text

    def set_pub_date(self, new_date):
        self.pub_date = new_date
        self.save()
        return self.pub_date

    def set_importance(self):
        if self.is_important == True:
            self.is_important = False
        else:
            self.is_important = True
        self.save()
        return self.is_important

    def __str__(self):
        return self.folder_text

"""
    def get_tags(self):
        return self.tags

    def get_creator(self):
        return self.creator

    def get_folder_text(self):
        return self.folder_text

    def get_pub_date(self):
        return self.pub_date
        
    def get_importance(self):
        return self.is_important
"""
class Source(models.Model): #source object

    folders_contained_in = models.ManyToManyField(Folder) # using foreign key creates a list type thing for the key object, called "(the key).(the keyed obj)_set"
    source_text = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=datetime.datetime.now, editable=True)
    pub_date = models.DateField(null=True, editable=True)
    source_url = models.URLField(null = True)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)


    def set_source_text(self, new_text):
        self.source_text = new_text
        self.save()
        return

    def set_date_added(self, new_date_add):
        self.date_added = new_date_add
        self.save()
        return

    def set_date_published(self, new_date_pub):
        self.pub_date = new_date_pub
        self.save()
        return

    def set_tags(self, new_tags):
        self.tags = new_tags
        self.save()
        return

    def set_source(self, new_url):
        self.source_url = new_url
        self.save()
        return

    def set_description(self, new_description):
        self.description = new_description
        self.save()
        return

    def set_author(self, new_author):
        self.author = new_author
        self.save()
        return

    def __str__(self):
        return self.source_text



#profile start

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=10, default= "None", null=True)
    bio = models.TextField(default='', blank=True)

    def get_username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username
        self.user.save()
        return

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
        self.user.save()
        return

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
        self.user.save()
        return

    def set_email(self, new_email):
        self.email = new_email
        self.user.save()
        return

    def set_gender(self, new_gender):
        self.gender = new_gender
        self.save()
        return

    def set_bio(self, new_bio):
        self.bio = new_bio
        self.save()
        return

    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


#profile end
