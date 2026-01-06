from django.contrib import admin

from Entries.models import EntryV1, CreateCode

@admin.register(EntryV1)
class EntryAdmin(admin.ModelAdmin):
    pass

@admin.register(CreateCode)
class CreateCodeAdmin(admin.ModelAdmin):
    pass
