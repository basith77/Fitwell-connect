# Generated by Django 3.1.2 on 2021-04-02 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='imagepath',
            field=models.CharField(default='', max_length=100),
        ),
    ]