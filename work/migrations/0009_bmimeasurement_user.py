# Generated by Django 2.2 on 2022-04-03 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_auto_20220403_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmimeasurement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.Register'),
        ),
    ]
