from django.db import models

# Create your models here.

class Case(models.Model):
    case_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    # Additional fields as needed

    def __str__(self):
        return self.case_number

