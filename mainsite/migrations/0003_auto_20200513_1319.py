# Generated by Django 3.0.3 on 2020-05-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20200513_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foyer',
            name='telephone',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
