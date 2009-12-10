from django.conf.urls.defaults import patterns, include, handler500, url
urlpatterns = patterns(
    'todo.views',
    url(r'^$', 'todo_list_all', name='todo-list-all'),
    url(r'^(?P<slug>[a-zA-Z0-9\-_]+)/$', 'todo_list', name='todo-list-detail'),
    url(r'^(?P<slug>[a-zA-Z0-9\-_]+)/(?P<pk>\d+)/$', 'todo_list_item', name='todo-list-item'),
)
