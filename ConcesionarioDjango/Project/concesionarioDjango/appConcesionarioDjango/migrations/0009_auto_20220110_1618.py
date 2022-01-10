# Generated by Django 3.2.9 on 2022-01-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appConcesionarioDjango', '0008_auto_20211114_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='coche',
            name='Combustibles',
        ),
        migrations.AddField(
            model_name='coche',
            name='combustibles',
            field=models.ManyToManyField(to='appConcesionarioDjango.Combustible'),
        ),
    ]
