# Generated by Django 3.1.5 on 2021-04-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210330_1210'),
        ('advisement', '0018_auto_20210430_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisee',
            name='advisors',
            field=models.ManyToManyField(to='accounts.Faculty'),
        ),
    ]
