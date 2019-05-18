# Generated by Django 2.2 on 2019-05-16 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_main', models.BooleanField(default=False, help_text="Should we display these details as                                   main product's details ? <br><b>Note : one                                   product should be set as main</b>")),
                ('color', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='shoestore/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.Product')),
            ],
            options={
                'verbose_name': 'Child Product',
                'verbose_name_plural': 'Child Products',
                'ordering': ['-timestamp'],
            },
        ),
    ]
