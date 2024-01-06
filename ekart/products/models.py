from django.db import models

# Product model

class Products(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    title = models.CharField(max_length = 200)
    price = models.FloatField()
    description = models.models.TextField()
    image = models.ImageField(upload_to='/media')
    priority = models.models.IntegerField(default=0)
    delete_status = models.models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title
    