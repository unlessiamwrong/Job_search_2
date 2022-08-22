from django.contrib.auth.models import User

from django.db.models import CASCADE, CharField, DateField, ForeignKey, ImageField, IntegerField, Model, OneToOneField, \
    SlugField, TextChoices, TextField


class Vacancy(Model):
    title = CharField(max_length=100)
    specialty = ForeignKey('Specialty', on_delete=CASCADE, related_name='vacancies')
    company = ForeignKey('Company', on_delete=CASCADE, related_name='vacancies')
    skills = TextField()
    description = TextField()
    salary_min = IntegerField()
    salary_max = IntegerField()
    published_at = DateField()

    def __str__(self):
        return self.title


class Company(Model):
    name = CharField(max_length=100)
    location = CharField(max_length=100)
    logo = ImageField(upload_to='company_images/')
    description = TextField()
    employee_count = IntegerField()
    owner = OneToOneField(User, on_delete=CASCADE, default=None, null=True)


class Specialty(Model):
    code = SlugField(max_length=300)
    title = CharField(max_length=100)
    picture = ImageField(upload_to='specialty_images/')

    def __str__(self):
        return self.title


class Application(Model):
    written_username = CharField(max_length=20)
    written_phone = IntegerField()
    written_cover_letter = TextField()
    vacancy = ForeignKey(Vacancy, on_delete=CASCADE, related_name='applications', default=None, null=True)
    user = ForeignKey(User, on_delete=CASCADE, related_name='applications', default=None, null=True)


class Resume(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='resumes')
    name = CharField(max_length=20)
    surname = CharField(max_length=20)

    class Status(TextChoices):
        NOT_SEARCHING = '1', 'Не ищу работу'
        CONSIDERING = '2', 'Рассматриваю предложения'
        SEARCHING = '3', 'Ищу работу'

    status = CharField(max_length=30, choices=Status.choices, default=Status.SEARCHING)

    salary = IntegerField()
    specialty = ForeignKey('Specialty', on_delete=CASCADE, related_name='resumes')

    class Grade(TextChoices):
        TRAINEE = '1', 'Стажер'
        JUNIOR = '2', 'Джуниор'
        MIDDLE = '3', 'Мидл'
        SENIOR = '4', 'Синьор'
        LEAD = '5', 'Лид'

    grade = CharField(max_length=20, choices=Grade.choices, default=Grade.TRAINEE)

    education = TextField()
    experience = TextField()
    portfolio = TextField()
