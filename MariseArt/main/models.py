from django.db import models


class Picture(models.Model):
    picture = models.ImageField(null=True, default='default_image.jpg', blank=True)
    name = models.CharField(max_length=200, null=True, default="picture")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class PortfolioPicture(models.Model):
    picture = models.ForeignKey(Picture, null=True, blank=True, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True, default=0)
    dislikes = models.IntegerField(null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.picture.name


class ShopPicture(models.Model):
    picture = models.ForeignKey(Picture, null=True, blank=True, on_delete=models.CASCADE)
    price = models.FloatField(null=True, default=0)
    sells = models.IntegerField(null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.picture.name
