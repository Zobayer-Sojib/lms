from django.contrib import admin
from .models import book,BookDB

# Register your models here.

admin.site.register(book)
admin.site.register(BookDB)