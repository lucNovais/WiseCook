# Generated by Django 3.1.7 on 2021-04-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('restricoes', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]