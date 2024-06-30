# Generated by Django 5.0.6 on 2024-06-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField()),
                ('salary', models.FloatField()),
                ('education', models.CharField(max_length=50)),
            ],
        ),
    ]
