# Generated by Django 2.2.6 on 2019-10-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrase', '0004_auto_20191023_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrase',
            name='category',
            field=models.CharField(choices=[('Romance', 'Romance'), ('Fiction', 'Fiction'), ('Politics', 'Politics'), ('Fantasy', 'Fantasy'), ('Social', 'Social'), ('Other', 'Other')], default='Romance', max_length=30),
        ),
    ]
