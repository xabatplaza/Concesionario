# Generated by Django 3.2.9 on 2021-11-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appConcesionarioDjango', '0003_auto_20211111_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='info',
            field=models.CharField(default='SOME STRING', max_length=180),
        ),
    ]