from django.db import models
class Article(models.Model):
    title=models.CharField(max_length=32)
    content=models.TextField(max_length=512,null=True)
    def __str__(self):
        return  self.title
