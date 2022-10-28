from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, help_text='Enter the post title')
    author = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    main_text = models.TextField(max_length=15000, help_text='Write what you think')
    topic = models.ManyToManyField('Topic', help_text='Select a topic for the post')
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    # help_text="Unique ID for this particular post across the site")
    # posted date
    posted = models.DateField(auto_now=True)

    def get_absolute_url(self):
        # 'view-post' to click and see on the post and see it`s details
        # return reverse('view-post', kwargs={'pk': self.pk})
        # return f'/allposts/{self.pk}/'

        return reverse('view-post', args=[str(self.id)])

    def __str__(self):
        return self.title

    def display_topic(self):
        return ', '.join([topic.name for topic in self.topic.all()[:3]])

    display_topic.short_description = 'Topic'


class Topic(models.Model):
    name = models.CharField(max_length=50, help_text='Enter a post topic')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('topic-detail', args=[str(self.id)])


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


