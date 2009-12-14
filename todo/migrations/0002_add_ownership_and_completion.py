
from south.db import db
from django.db import models
from todo.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'List.owner'
        db.add_column('todo_list', 'owner', models.ForeignKey(orm['auth.User'], default=1))
        
        # Adding field 'Item.is_done'
        db.add_column('todo_item', 'is_done', models.BooleanField(default=False))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'List.owner'
        db.delete_column('todo_list', 'owner_id')
        
        # Deleting field 'Item.is_done'
        db.delete_column('todo_item', 'is_done')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'todo.item': {
            'Meta': {'ordering': "['order',]"},
            'goal': ('models.CharField', [], {'max_length': '255'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_done': ('models.BooleanField', [], {'default': 'False'}),
            'list': ('models.ForeignKey', ["orm['todo.List']"], {}),
            'order': ('models.PositiveIntegerField', [], {'default': '0'}),
            'when': ('models.DateTimeField', [], {})
        },
        'todo.list': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255'}),
            'owner': ('models.ForeignKey', ["orm['auth.User']"], {}),
            'slug': ('models.SlugField', [], {'unique': 'True'})
        }
    }
    
    complete_apps = ['todo']
