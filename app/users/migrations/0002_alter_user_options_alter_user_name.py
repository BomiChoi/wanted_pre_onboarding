# Generated by Django 4.1 on 2022-08-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=10, verbose_name='이름'),
        ),
    ]
