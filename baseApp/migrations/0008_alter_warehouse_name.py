# Generated by Django 3.2.5 on 2022-06-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0007_auto_20220620_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]