from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    mobile = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(max_length=50)

    def __str__(self) -> str:
        return self.name
