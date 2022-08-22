# Generated by Django 4.1 on 2022-08-18 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=pathlib.PureWindowsPath('C:/Users/Вячеслав/stepik_tours_3/company_images')),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to=pathlib.PureWindowsPath('C:/Users/Вячеслав/stepik_tours_3/speciality_images')),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('1', 'Не ищу работу'), ('2', 'Рассматриваю предложения'), ('3', 'Ищу работу')], default='3', max_length=30)),
                ('salary', models.IntegerField()),
                ('grade', models.CharField(choices=[('1', 'Стажер'), ('2', 'Джуниор'), ('3', 'Мидл'), ('4', 'Синьор'), ('5', 'Лид')], default='1', max_length=20)),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('portfolio', models.TextField()),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='vacancy.specialty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=20)),
                ('written_phone', models.IntegerField()),
                ('written_cover_letter', models.TextField()),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='vacancy.vacancy')),
            ],
        ),
    ]
