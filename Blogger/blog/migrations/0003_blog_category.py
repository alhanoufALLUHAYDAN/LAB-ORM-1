# Generated by Django 5.1.2 on 2024-11-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image_alter_blog_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('NAT', 'Nature'), ('PHY', 'Physics'), ('CHE', 'Chemistry'), ('PLA', 'Plants'), ('MTH', 'Mathematics'), ('SCI', 'Science')], default='SCI', max_length=4),
        ),
    ]
