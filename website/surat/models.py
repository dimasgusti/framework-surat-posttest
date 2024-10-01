from django.db import models
from datetime import datetime

class Sender(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    no_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    
    def __str__(self):
        return self.nama
    
class Letter(models.Model):
    judul = models.CharField(max_length=200)
    pesan = models.TextField()
    tanggal = models.DateField(default=datetime.now)
    pengirim = models.ForeignKey(Sender, on_delete=models.CASCADE, related_name='surat')
    
    def __str__(self):
        return self.judul