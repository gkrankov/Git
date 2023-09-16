from django.db import models

class Couple(models.Model):
    bride_name = models.CharField(max_length=100)
    groom_name = models.CharField(max_length=100)
    wedding_date = models.DateField()
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.bride_name} & {self.groom_name}"
