from django.contrib import admin
from django.contrib.auth.models import User
from .models import Sender, Letter

class SenderModel(admin.ModelAdmin):
    list_display = ('nama', 'email', 'no_hp', 'alamat')
    search_fields = ('nama', 'email')
    list_filter = ('no_hp',)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            User.objects.create_user(
                username=obj.email,
                email=obj.email,
                password='defaultpassword'
            )

class LetterModel(admin.ModelAdmin):
    list_display = ('judul', 'tanggal', 'pengirim')
    search_fields = ('judul', 'isi')
    list_filter = ('tanggal', 'pengirim')

admin.site.register(Sender, SenderModel)
admin.site.register(Letter, LetterModel)