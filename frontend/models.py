from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('GTX1080ti', 'GTX1080ti'),
    ('GTX2080ti', 'GTX2080ti'),
    ('GTX3080ti', 'GTX3080ti'),
     ('GTX3090ti', 'GTX3090ti'),
     ('GTX4090ti', 'GTX4090ti'),
)

# product models
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'

# order models
class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'

# profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'