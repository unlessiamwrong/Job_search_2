from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, ChoiceField, FileInput, ImageField, IntegerField, ModelChoiceField, ModelForm, \
    PasswordInput, Select, Textarea, TextInput

from vacancy.models import Application, Company, Vacancy, Specialty, Resume


class ApplicationForm(ModelForm):
    written_username = CharField(max_length=20, label='Вас зовут', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    written_phone = IntegerField(label='Ваш телефон', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    written_cover_letter = CharField(label='Сопроводительное письмо', widget=Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']


class CompanyForm(ModelForm):
    name = CharField(max_length=20, label='Название компании', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    location = CharField(max_length=20, label='География', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = CharField(label='Информация о компании', widget=Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    employee_count = CharField(label='Количество человек в компании', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    logo = ImageField(label='Логотип', widget=FileInput(
        attrs={
            'class': 'custom-file-input',
        }
    ))

    class Meta:
        model = Company
        fields = ['name', 'location', 'description', 'employee_count', 'logo']


class VacancyForm(ModelForm):
    title = CharField(max_length=20, label='Название вакансии', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    skills = CharField(max_length=20, label='Требуемые навыки', widget=Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    description = CharField(label='Описание вакансии', widget=Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    salary_min = IntegerField(label='Зарплата от', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    salary_max = IntegerField(label='Зарплата до', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    specialty = ModelChoiceField(label='Специализация', queryset=Specialty.objects.all(), widget=Select(
        attrs={
            'class': 'custom-select mr-sm-2',
        }
    ))

    class Meta:
        model = Vacancy
        fields = ['title', 'skills', 'description', 'salary_min', 'salary_max', 'specialty']


class ResumeForm(ModelForm):
    name = CharField(max_length=20, label='Имя', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    surname = CharField(max_length=20, label='Фамилия', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    status = ChoiceField(label='Готовность к работе', choices=Resume.Status.choices, widget=Select(
        attrs={
            'class': 'custom-select mr-sm-2',
        }
    ))
    salary = CharField(max_length=20, label='Ожидаемое вознаграждение', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    specialty = ModelChoiceField(label='Специализация', queryset=Specialty.objects.all(), widget=Select(
        attrs={
            'class': 'custom-select mr-sm-2',
        }
    ))
    grade = ChoiceField(label='Квалификация', choices=Resume.Grade.choices, widget=Select(
        attrs={
            'class': 'custom-select mr-sm-2',
        }
    ))
    education = CharField(label='Образование', widget=Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    experience = CharField(label='Опыт работы', widget=Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    portfolio = CharField(label='Ссылка на портфолио', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']


class SignUpForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    first_name = CharField(label='Имя', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    last_name = CharField(label='Фамилия', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password1 = CharField(label='Пароль', widget=PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password2 = CharField(label='Подтверждение пароля', widget=PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class MyAuthenticationForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password = CharField(label='Пароль', widget=PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password']
