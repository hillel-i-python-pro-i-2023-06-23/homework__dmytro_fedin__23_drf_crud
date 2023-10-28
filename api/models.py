from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    name = models.CharField(max_length=20, unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?[-().\dx]{9,20}$",
        message="Phone number is invalid",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
