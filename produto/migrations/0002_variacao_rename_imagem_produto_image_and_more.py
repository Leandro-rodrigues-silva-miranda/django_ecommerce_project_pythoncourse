# Generated by Django 5.0.1 on 2024-01-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='imagem',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='descricao_longa',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='preco_marketing',
            new_name='promotional_mkt_price',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='descricao_curta',
            new_name='short_description',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='tipo',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='preco_marketing_promocional',
        ),
        migrations.AddField(
            model_name='produto',
            name='mkt_price',
            field=models.FloatField(default=0),
        ),
    ]
