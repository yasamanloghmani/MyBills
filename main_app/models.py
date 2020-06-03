from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

class Bill(models.Model):
    EXPENSE = 'exp'
    INCOME = 'inc'
    CATAGORY_CHOICES = (
        (EXPENSE, 'expense'),
        (INCOME, 'income')
    )
    title = models.CharField(max_length=100)
    catagory = models.CharField(max_length=3, choices=CATAGORY_CHOICES)
    amount = models.IntegerField()
    description = models.TextField(max_length=250)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title