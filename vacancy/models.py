from django.db import models
from django.db.models import CharField, DateField, ForeignKey, IntegerField, SlugField, TextField, URLField


class Vacancy(models.Model):
    title = CharField(max_length=100)
    specialty = ForeignKey('Specialty', on_delete=models.CASCADE, related_name="vacancies")
    company = ForeignKey('Company', on_delete=models.CASCADE, related_name="vacancies")
    skills = TextField()
    description = TextField()
    salary_min = IntegerField()
    salary_max = IntegerField()
    published_at = DateField()


class Company(models.Model):
    name = CharField(max_length=100)
    location = CharField(max_length=100)
    logo = URLField(default='https://place-hold.it/100x60')
    description = TextField()
    employee_count = IntegerField()


class Specialty(models.Model):
    code = SlugField(max_length=300)
    title = CharField(max_length=100)
    picture = URLField(default='https://place-hold.it/100x60')
