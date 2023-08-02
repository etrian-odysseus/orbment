# Generated by Django 4.2.3 on 2023-08-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbment_list', '0004_alter_attribute_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orbment',
            old_name='attribute_type',
            new_name='attributes',
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='attribute_type',
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_name',
            field=models.CharField(default='STR', max_length=100, verbose_name='Attribute Name'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AttributeType',
        ),
    ]