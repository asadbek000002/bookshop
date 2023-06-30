from django.db import models
from django.contrib.auth.models import User



# saqlanganlar modeli kitobni saqlash uchun

class Saved(models.Model):
    book = models.ForeignKey("myapp.Kitob", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} | saved | {self.book.sarlavha}"


