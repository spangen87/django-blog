from django.db import models


class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    time = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
