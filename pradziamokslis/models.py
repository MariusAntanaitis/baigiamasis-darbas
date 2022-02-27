from django.db import models

class Mokinys(models.Model):
    vardas = models.CharField(max_length=30)
    pavarde = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    telefono_numeris = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = "Mokiniai"

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

    