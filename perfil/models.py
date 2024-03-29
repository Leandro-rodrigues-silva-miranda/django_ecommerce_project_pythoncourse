from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re

from utils.validator import valida_cpf,calc_age


class Profile(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True,blank=True)
    birthday = models.DateField()  
    cpf = models.CharField(max_length=11,help_text='Somente números')
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30,blank=True,null=True)
    neighborhood = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        default='MG',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            )
        )
    
    def clean(self):
        self.age=calc_age(self.birthday.year,self.birthday.month,self.birthday.day)

        error_messages = {}

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'

        if re.search(r'[^0-9]',self.cep) or len(self.cep) != 8:
            error_messages['cep'] = 'Digite um CEP válido'

        if error_messages:
            raise ValidationError(error_messages)


    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'\
              if self.user.first_name else f'{self.user.username}'
