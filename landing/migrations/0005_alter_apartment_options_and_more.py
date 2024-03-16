# Generated by Django 4.2.11 on 2024-03-16 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_apartment_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'apartment', 'verbose_name_plural': 'apartments'},
        ),
        migrations.AlterModelOptions(
            name='apartmentuserform',
            options={'verbose_name': 'apartment user form', 'verbose_name_plural': 'apartment user forms'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'banner', 'verbose_name_plural': 'banners'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.AlterModelOptions(
            name='userform',
            options={'verbose_name': 'user form', 'verbose_name_plural': 'user forms'},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='address',
            field=models.CharField(max_length=128, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='location_lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='location_long',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='longtitude'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='room_number',
            field=models.IntegerField(verbose_name='room_number'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='size_in_m2',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='size'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='status',
            field=models.CharField(choices=[('on sale', 'on sale'), ('unavailable', 'unavailable')], default=('on sale', 'on sale'), max_length=15, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='apartmentuserform',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='apartment', to='landing.apartment'),
        ),
        migrations.AlterField(
            model_name='apartmentuserform',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='apartmentuserform',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='apartmentuserform',
            name='phone_number',
            field=models.CharField(max_length=14, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='apartmentuserform',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('connected', 'connected'), ('pending', 'Pending')], default=('new', 'new'), max_length=10, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='media/banner', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.ImageField(upload_to='media/apartments', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='images',
            name='main',
            field=models.BooleanField(default=False, verbose_name='main'),
        ),
        migrations.AlterField(
            model_name='userform',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='userform',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='userform',
            name='phone_number',
            field=models.CharField(max_length=14, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='userform',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('connected', 'connected'), ('pending', 'Pending')], default=('new', 'new'), max_length=10, verbose_name='status'),
        ),
        migrations.CreateModel(
            name='MobileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='media/apartments', verbose_name='file')),
                ('main', models.BooleanField(default=False, verbose_name='main')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mobile_images', to='landing.apartment')),
            ],
        ),
    ]