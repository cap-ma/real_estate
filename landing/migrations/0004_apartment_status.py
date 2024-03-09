# Generated by Django 4.2.11 on 2024-03-09 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_apartmentuserform_status_userform_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='status',
            field=models.CharField(choices=[('on sale', 'on sale'), ('unavailable', 'unavailable')], default=('on sale', 'on sale'), max_length=15),
        ),
    ]