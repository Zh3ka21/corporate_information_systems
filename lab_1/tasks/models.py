from django.db import models

class CssParameters(models.Model):
    margin = models.CharField(max_length=50)
    padding = models.CharField(max_length=50)
    block_size = models.CharField(max_length=50)

    def __str__(self):
        return f"Margin: {self.margin}, Padding: {self.padding}, Size: {self.block_size}"

