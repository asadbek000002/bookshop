from django.db import models
from django.contrib.auth.models import User



class Kitob(models.Model):
    rasm = models.ImageField(upload_to='kitoblar/', blank=True)
    sarlavha = models.CharField(max_length=255)
    muallif = models.CharField(max_length=255)
    tarif = models.TextField()
    narx = models.IntegerField()
    mavjud_miqdor = models.IntegerField()

    def __str__(self):
        return self.sarlavha

class Buy(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE, null=True)
    yetkasiz = models.CharField(max_length=100)
    hudun = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




