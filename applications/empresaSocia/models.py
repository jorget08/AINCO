from django.db import models

# Create your models here.

class EmpresaSocia(models.Model):
    nombre = models.CharField(max_length=250)

    def _str_(self):
        return self.nombre