from django.contrib import admin
from models import List, Item

class ListAdmin(admin.ModelAdmin):
    exclude = ('owner',)
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'owner',)
    def save_model(self, request, obj, form, change):
        if request.POST.get('owner', None) is None:
            obj.owner = request.user
        return super(ListAdmin, self).save_model(request, obj, form, change) 

class ItemAdmin(admin.ModelAdmin):
    list_display = ('goal', 'list', 'is_done',)
    list_filter = ('is_done', 'list',)

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)
