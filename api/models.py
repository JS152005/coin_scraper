from django.db import models
import uuid
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

class ScrapingJob(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scraping Job {self.job_id}"

class ScrapingTask(models.Model):
    job = models.ForeignKey(ScrapingJob, related_name='tasks', on_delete=models.CASCADE)
    coin = models.CharField(max_length=100)
    output = JSONField(null=True, blank=True)
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scraping Task for {self.coin}"