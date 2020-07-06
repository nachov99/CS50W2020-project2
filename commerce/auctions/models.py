from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Banned', 'Banned'),
        ('Finished', 'Finished'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    imgurl = models.CharField(max_length=256)
    min_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=8, choices=STATUS, default='Active')

    def __str__(self):
        return f"{self.category} - {self.title} ${self.min_price}"

class Bid(models.Model):
    STATUS = (
        ('Winning', 'Winning'),
        ('Lossing', 'Lossing'),
    )
    item_id = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bid = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=7, choices=STATUS)

    def __str__(self):
        return f"{self.item_id} {self.user} ${self.bid}"

class Comment(models.Model):
    item_id = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.item_id} {self.user_id} {self.msg}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Listing)

    def __str__(self):
        return f" Watchlist id: {self.id} - Customer: {self.user}"