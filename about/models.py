from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, help_text="About My Blog")
    content = models.TextField(help_text="This is the About page content")
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
