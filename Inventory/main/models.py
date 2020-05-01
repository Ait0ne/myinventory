from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django import forms


# Create your models here.
class Layout(models.Model):
    user = models.ForeignKey(User,default=1,on_delete = models.CASCADE, null=True)
    position_layout = models.CharField(max_length=100, default='No location')

    def __str__(self):
        return f'{self.position_layout}'

    def get_absolute_url(self):
        return reverse('layout-create')

    # def save(self, *args, **kwargs):
    #     self.user = self.request.user
    #     super(Layout,self).save(*args,**kwargs)



class Item(models.Model):
    type_choices = [
        ('Shoes', 'Shoes'),
        ('Blouse', 'Blouse'),
        ('Skirt', 'Skirt'),
        ('Shirt', 'Shirt'),
        ('Accessory', 'Accessory'),
        ('Hat', 'Hat'),
        ('T-shirt', 'T-shirt'),
        ('Tie','Tie'),
        ('Boots', 'Boots'),
        ('Pants', 'Pants'),
        ('Sweater', 'Sweater'),
        ('Polo-shirt', 'Polo-shirt'),
        ('Hoodie', 'Hoodie'),
        ('Coat', 'Coat'),
        ('Underwear', 'Underwear'),
        ('Kitchenware', 'Kitchenware'),
        ('instrument', 'Instrument'),
        ('Socks', 'Socks'),
        ('Jacket', 'Jacket'),
        ('Overcoat', 'Overcoat'),
    ]
    type_choices.sort()
    type_choices.append(('Other','Other'))

    image = models.ImageField(default='111.jpg',upload_to='uploads')
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=type_choices, default='Shoes')
    position_item = models.ForeignKey(Layout, on_delete=models.SET_NULL, null=True, related_name='position_layout+', verbose_name='Location')
    size = models.CharField(max_length=100, default='No size')
    info = models.TextField(default='No details')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,default=1,on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item-detail',kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height >300 or img.width > 300:
            if img.height<img.width:
                img = img.rotate(270,expand=True)
            output_size = (225,300)
            img.resize(output_size)

            img.save(self.image.path)

