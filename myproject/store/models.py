from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Goods(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='goods_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    author = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField(5000)
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.goods}'

