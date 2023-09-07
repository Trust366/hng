from django.db import models
from django.utils import timezone
# Create your models here.

class Details(models.Model):
    slack_name = models.CharField(max_length=255)
    current_day = models.CharField(max_length=10) 
    utc_time = models.DateField(default=timezone.now)
    track = models.CharField(max_length=255)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
    status_code = models.PositiveIntegerField() 

    def __str__(self):
        return self.slack_name 
