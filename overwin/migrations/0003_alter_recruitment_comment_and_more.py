# Generated by Django 4.2 on 2024-05-31 05:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overwin', '0002_alter_joinedmember_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='comment',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='備考欄'),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='max_recruit_member',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='募集人数'),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='募集者'),
        ),
    ]
