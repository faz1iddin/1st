from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 150)
    author = models.ForeignKey(
        "auth.user",
        on_delete = models.CASCADE
    )
    text = models.TextField()


  
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('home_detail', args = [str(self.pk)])