from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class Product(models.Model):
    product_code = models.CharField(max_length=30, verbose_name='Ürün Kodu')
    name = models.CharField(max_length=120, verbose_name='Ürün Adı')
    stock = models.IntegerField(verbose_name='Ürün Adedi')
    price = models.FloatField(verbose_name='Ürün Fiyatı')
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'slug':self.slug})

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Product, self).save(*args,**kwargs)