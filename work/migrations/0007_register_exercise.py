# Generated by Django 3.1.6 on 2021-03-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_cart_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Exercise',
            field=models.CharField(choices=[('Muscle Gaining', 'Muscle Gaining'), ('Palete', 'Palete'), ('Yoga', 'Yoga'), ('Barre', 'Barre'), ('Crossfit', 'Crossfit')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
