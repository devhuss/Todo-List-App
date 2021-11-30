from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    updated = models.BooleanField(default=False)

    def __str__(self):
    
        return self.text + str(self.id)

