from django.db import models

class Empolyee(models.Model):
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('others', 'Others'),
    ]

    name = models.CharField(max_length=100, blank=False)
    pan = models.CharField(max_length=10, unique=True)  # Assuming PAN should be unique
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)  # Emails should likely also be unique
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Empolyee'
        verbose_name_plural = 'Empolyees'

    def __str__(self):
        return f"{self.name} - {self.email}"



