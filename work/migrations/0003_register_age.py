# Generated by Django 3.1.6 on 2021-02-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_review_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Age',
            field=models.PositiveIntegerField(default=int),
            preserve_default=False,
        ),
    ]