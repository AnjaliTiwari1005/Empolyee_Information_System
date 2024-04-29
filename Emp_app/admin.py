from django.contrib import admin
from .models import Empolyee

class EmpolyeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pan', 'age', 'gender', 'email', 'city')  # Columns to display in the admin list view
    list_filter = ('gender', 'city')  # Filters on the right sidebar for easy sorting
    search_fields = ('name', 'pan', 'email')  # Fields to search in the admin
    ordering = ('name',)  # Default ordering

admin.site.register(Empolyee, EmpolyeeAdmin)



