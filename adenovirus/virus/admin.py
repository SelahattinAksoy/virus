from django.contrib import admin
from .models import Virus,Announcement,Adenovirus,Coronavirus,Influenza,Publication
from import_export.admin import ImportExportModelAdmin

admin.site.register(Virus)
admin.site.register(Announcement)
#admin.site.register(Adenovirus)
#admin.site.register(Coronavirus)
admin.site.register(Influenza)
#admin.site.register(Publication)

@admin.register(Adenovirus,Coronavirus,Publication)
class ViewAdmin(ImportExportModelAdmin):
    pass