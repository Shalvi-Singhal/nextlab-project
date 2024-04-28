from django.contrib import admin
from .models import App,Profile,TaskCompletion

# Register your models here
admin.site.register(App)
admin.site.register(Profile)
admin.site.register(TaskCompletion)