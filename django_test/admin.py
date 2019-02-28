from django.contrib import admin
from django_test.models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('name',)