# Generated by Django 2.0.3 on 2018-07-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_course_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('i', 'In Progress'), ('r', 'Review'), ('p', 'Published')], default='i', max_length=1),
        ),
    ]