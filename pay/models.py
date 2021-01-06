from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Bills(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='bills')
    count = models.FloatField()
    state = models.BooleanField(default=False)
