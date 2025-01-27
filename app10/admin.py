from django.contrib import admin
from .models import Register1

# Register your models here.
class signup(admin.ModelAdmin):
    list_display=('mobile','full_name')

admin.site.register(Register1,signup)
