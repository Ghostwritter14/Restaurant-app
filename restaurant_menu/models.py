from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_course", "Main Course"),
    ("desserts", "Desserts"),
    ("drinks", "Drinks")
)

# Whether the meal is available or not
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


# Create your models here.
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)  # avoiding duplication of meals
    description = models.CharField(max_length=3000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=150, choices=MEAL_TYPE)
    author = models.ForeignKey(User, models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)  # whenever a cook adds an item the timestamp is recorded
    date_updated = models.DateTimeField(auto_now=True)  # the time when an item is updated

    def __str__(self):
        return self.meal
