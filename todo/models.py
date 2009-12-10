from django.db import models
from django.core.urlresolvers import reverse

class List(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s'%self.name

    def get_absolute_url(self):
        return reverse('todo-list-detail', kwargs={'slug':self.slug})

class Item(models.Model):
    goal = models.CharField(max_length=255)
    when = models.DateTimeField()
    list = models.ForeignKey(List)
    order = models.PositiveIntegerField(default=0)
    def __unicode__(self):
        return u'%s'%self.goal

    def get_absolute_url(self):
        return reverse('todo-list-item', kwargs={'slug':self.list.slug, 'pk':self.pk})
