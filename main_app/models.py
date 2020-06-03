from django.db import models
from django.utils import timezone
from django.models import fields
from django.contrib.auth.models import User

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
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = fields.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title