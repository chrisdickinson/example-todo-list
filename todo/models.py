from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class List(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s'%self.name

    def get_absolute_url(self):
        return reverse('todo-list-detail', kwargs={'slug':self.slug})

    def is_done(self):
        is_done = reduce(lambda x, y: x and y.is_done, self.item_set.all(), True)
        return is_done

class Item(models.Model):
    goal = models.CharField(max_length=255)
    when = models.DateTimeField()
    list = models.ForeignKey(List)
    order = models.PositiveIntegerField(default=0)
    is_done = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s'%self.goal

    def get_absolute_url(self):
        return reverse('todo-list-item', kwargs={'slug':self.list.slug, 'pk':self.pk})
    class Meta:
        ordering = ['order',]
