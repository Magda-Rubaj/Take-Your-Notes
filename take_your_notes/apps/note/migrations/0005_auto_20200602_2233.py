# Generated by Django 3.0.6 on 2020-06-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20200602_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]