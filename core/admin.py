from django.contrib import admin
from .models import *

# Register your models here.

class Filter(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'grade', 'birthday',)
    list_filter = ('birthday',)

admin.site.register(Student, Filter)