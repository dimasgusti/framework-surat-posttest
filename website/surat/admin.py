from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Sender, Letter

class SenderModel(admin.ModelAdmin):
    list_display = ('nama', 'email', 'no_hp', 'alamat')
    search_fields = ('nama', 'email')
    list_filter = ('no_hp',)

class LetterModel(admin.ModelAdmin):
    list_display = ('judul', 'tanggal', 'pengirim')
    search_fields = ('judul', 'isi')
    list_filter = ('tanggal', 'pengirim')

admin.site.register(Sender, SenderModel)
admin.site.register(Letter, LetterModel)