from django.contrib import admin
from .models import Phrase

# Register your models here.

class PhraseAdmin(admin.ModelAdmin):
    list_display = ('user','title','phrase','date')

admin.site.register(Phrase,PhraseAdmin)    
