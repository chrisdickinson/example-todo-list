
from south.db import db
from django.db import models
from todo.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Item'
        db.create_table('todo_item', (
            ('id', models.AutoField(primary_key=True)),
            ('goal', models.CharField(max_length=255)),
            ('when', models.DateTimeField()),
            ('list', models.ForeignKey(orm.List)),
            ('order', models.PositiveIntegerField(default=0)),
        ))
        db.send_create_signal('todo', ['Item'])
        
        # Adding model 'List'
        db.create_table('todo_list', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=255)),
            ('slug', models.SlugField(unique=True)),
        ))
        db.send_create_signal('todo', ['List'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Item'
        db.delete_table('todo_item')
        
        # Deleting model 'List'
        db.delete_table('todo_list')
        
    
    
    models = {
        'todo.item': {
            'goal': ('models.CharField', [], {'max_length': '255'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'list': ('models.ForeignKey', ["orm['todo.List']"], {}),
            'order': ('models.PositiveIntegerField', [], {'default': '0'}),
            'when': ('models.DateTimeField', [], {})
        },
        'todo.list': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'slug': ('models.SlugField', [], {'unique': 'True'})
        }
    }
    
    complete_apps = ['todo']
