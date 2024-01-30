from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A','Aprovado'),
            ('C','Criado'),
            ('R','Reprovado'),
            ('P','Pendente'),
            ('E','Enviado'),
            ('F','Finalizado')
            )
        )
    
    def __str__(self):
        return f'Pedido nº {self.pk}'
    
class ItemOrder(models.Model):
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do pedido'

    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'Produto {self.product_name} do pedido {self.order.pk}'
