# Generated by Django 4.2.4 on 2023-08-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('order_status', models.CharField(choices=[('received', 'Received'), ('preparing', 'Preparing'), ('ready', 'Ready for Pickup'), ('delivered', 'Delivered')], default='received', max_length=20)),
                ('dishes', models.ManyToManyField(to='menu.dish')),
            ],
        ),
    ]
