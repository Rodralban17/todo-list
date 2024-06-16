from django.contrib import admin
from .models import User, TemdieTask, TemdieTag
# Register your models here.

admin.site.register(User)
#admin.site.register(TemdieTask)
#admin.site.register(TemdieTag)

@admin.register(TemdieTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'completed')
    search_fields = ('title', 'description')
    list_filter = ('completed', 'due_date', 'temdietag__name')
    
@admin.register(TemdieTag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.site_header = "To-Do List Administration"
admin.site.site_title = "To-Do List Admin Portal"
admin.site.index_title = "Welcome to To-Do List Administration"