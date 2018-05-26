from django.db import models

class review(models.Model):
    response = models.CharField(max_length = 200)

    def __str__(self):
        return self.response



