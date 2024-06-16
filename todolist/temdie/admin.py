from django.contrib import admin
from .models import User, TemdieTask, TemdieTag
# Register your models here.

admin.site.register(User)
admin.site.register(TemdieTask)
admin.site.register(TemdieTag)

