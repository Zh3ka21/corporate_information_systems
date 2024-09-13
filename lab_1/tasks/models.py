from django.db import models

class CssParameters(models.Model):
    margin = models.CharField(max_length=50)
    padding = models.CharField(max_length=50)
    block_size = models.CharField(max_length=50)

    def __str__(self):
        return f"Margin: {self.margin}, Padding: {self.padding}, Size: {self.block_size}"

class Image(models.Model):
    url = models.URLField(max_length=100, unique=True)
    height = models.IntegerField()

    def __str__(self):
        return f"URL: {self.url}, Height: {self.height}, Width: {self.width}, Label: {self.label}"

