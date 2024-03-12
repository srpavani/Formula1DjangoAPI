
from django.db import models

class F1ResultModels(models.Model):
    GrandPix = models.CharField(verbose_name="GrandPix", max_length=30)
    data = models.CharField(verbose_name="data", max_length=30, blank = True, null = True)
    vencedor = models.CharField(verbose_name="vencedor", max_length=30, blank = True, null = True)
    time = models.CharField(verbose_name="time", max_length=30, blank = True, null = True)
    voltas = models.CharField(verbose_name="voltas", max_length=30, blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.GrandPix} {self.data} {self.vencedor} {self.time} {self.voltas}"
    

       
        
