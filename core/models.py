from django.db import models


class Email(models.Model):
    email = models.EmailField(blank=False)
    submitted_from = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = True


class Site(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=2000)
    vote_count = models.IntegerField(default=0)