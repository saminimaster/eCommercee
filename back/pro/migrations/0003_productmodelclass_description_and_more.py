# Generated by Django 4.0.3 on 2022-03-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0002_productmodelclass_name_productmodelclass_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodelclass',
            name='description',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
        migrations.AlterField(
            model_name='productmodelclass',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
