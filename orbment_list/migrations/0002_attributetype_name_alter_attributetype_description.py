# Generated by Django 4.2.3 on 2023-08-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbment_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributetype',
            name='name',
            field=models.CharField(default='STR', max_length=25, verbose_name='Attribute Type Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attributetype',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Attribute Type Description'),
        ),
    ]