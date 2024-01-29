from django.db import models
from PIL import Image
from django.conf import settings

# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    #Campos
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='produto_imagens/%Y/%m',blank=True,null=True)
    slug = models.SlugField(unique=True)
    mkt_price = models.FloatField(default=0)
    promotional_mkt_price = models.FloatField(null=True,blank=True)
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V','Variacao'),
            ('S','Simples')
            )
        )
    
    #Métodos sobrescritos
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            self.resizeImage()


    def __str__(self):
        return self.name
    
    #Métodos criados
    def resizeImage(self, new_width=800):
        image_path = settings.MEDIA_ROOT / self.image.name
        with Image.open(image_path) as image:
            original_width,original_height= image.size
            new_height = round((original_height*new_width)/original_width)
            if original_width > new_width:

                image = image.resize((new_width,new_height),Image.LANCZOS)
                image.save(image_path,optimize=True,quality=60)
        


class Variation(models.Model):
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'


    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True,null=True)
    price = models.FloatField()
    promotional_price = models.FloatField(null=True,blank=True)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name or self.product.name