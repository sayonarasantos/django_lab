from django.contrib import admin
from .models import ToDo, Tag, Task


class ToDoAdmin(admin.ModelAdmin):
    model = ToDo

    list_filter = ['tags', 'tasks']
    
    search_fields = ['name']
    
    list_display = ['name']


class TagAdmin(admin.ModelAdmin):
    model = Tag
    
    list_filter = ['color']


class TaskAdmin(admin.ModelAdmin):
    model = Task


admin.site.register(ToDo, ToDoAdmin)

admin.site.register(Tag, TagAdmin)

admin.site.register(Task, TaskAdmin)