import datetime

from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from vacancy.forms import ApplicationForm, CompanyForm, ResumeForm, VacancyForm
from vacancy.models import Application, Company, Resume, Specialty, Vacancy


def main_view(request: WSGIRequest) -> HttpResponse:
    context = {
        'companies': Company.objects.all(),
        'specialties': Specialty.objects.all()
    }
    return render(request, 'vacancy/index.html', context=context)


def vacancies_view(request: WSGIRequest) -> HttpResponse:
    context = {
        'vacancies': Vacancy.objects.all(),
        'specialties': Specialty.objects.all()
    }
    return render(request, 'vacancy/vacancies.html', context=context)


def specialty_view(request: WSGIRequest, specialty: str) -> HttpResponse:
    try:
        current_specialty = Specialty.objects.get(code=specialty)
    except Specialty.DoesNotExist:
        raise Http404
    context = {
        'specialty': current_specialty,
        'vacancies': Vacancy.objects.filter(specialty_id=current_specialty)
    }
    return render(request, 'vacancy/speciality.html', context=context)


def company_view(request: WSGIRequest, company_id: int) -> HttpResponse:
    try:
        current_company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        raise Http404
    context = {
        'company': current_company,
        'vacancies': Vacancy.objects.filter(company_id=current_company)
    }
    return render(request, 'vacancy/company.html', context=context)


def vacancy_view(request: WSGIRequest, vacancy_id: int) -> HttpResponse:
    try:
        current_vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vacancy = current_vacancy
            instance.user = request.user
            instance.save()
            return redirect('send_request', vacancy_id=vacancy_id)
    else:
        form = ApplicationForm()
    context = {
        'form': form,
        'vacancy': current_vacancy,
        'company': current_vacancy.company
    }
    return render(request, 'vacancy/vacancy.html', context=context)


def send_request_view(request: WSGIRequest, vacancy_id: int) -> HttpResponse:
    try:
        Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist:
        raise Http404
    return render(request, 'vacancy/sent.html')


def company_lets_start_view(request: WSGIRequest) -> HttpResponse:
    try:
        Company.objects.get(owner_id=request.user.id)
        return redirect('my_company')
    except Company.DoesNotExist:
        return render(request, 'vacancy/my_company/company_lets_start.html')


def create_company_view(request: WSGIRequest) -> HttpResponse:
    try:
        Company.objects.get(owner_id=request.user.id)
        return redirect('my_company')
    except Company.DoesNotExist:
        if request.method == 'POST':
            form = CompanyForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.owner = request.user
                instance.save()
        else:
            form = CompanyForm()
        return render(request, 'vacancy/my_company/create_company.html', {'form': form})


def my_company_view(request: WSGIRequest) -> HttpResponse:
    try:
        instance = Company.objects.get(owner_id=request.user.id)
        if request.method == 'GET':
            form = CompanyForm(instance=instance)
            return render(request, 'vacancy/my_company/my_company.html', {'form': form, 'company': instance})
        if request.method == 'POST':
            form = CompanyForm(request.POST, request.FILES, instance=instance)
            messages.success(request, 'Информация о компании обновлена')
            if form.is_valid():
                form.save()
            return redirect('my_company')
    except Company.DoesNotExist:
        return redirect('company_lets_start')


def my_company_vacancies_view(request: WSGIRequest) -> HttpResponse:
    current_company = Company.objects.get(owner_id=request.user.id)
    vacancies = Vacancy.objects.filter(company=current_company)
    for vacancy in vacancies:
        vacancy.applications_count = Application.objects.filter(vacancy=vacancy).count()
    return render(request, 'vacancy/my_company/my_company_vacancies.html', {'vacancies': vacancies})


def create_vacancy_view(request: WSGIRequest) -> HttpResponse:
    current_company = Company.objects.get(owner_id=request.user.id)
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = current_company
            instance.published_at = datetime.datetime.now()
            instance.save()
        return redirect('my_company_vacancies')
    else:
        form = VacancyForm()
        return render(request, 'vacancy/my_company/create_vacancy.html', {'form': form})


def my_company_vacancy_view(request: WSGIRequest, vacancy_id: int) -> HttpResponse:
    instance = Vacancy.objects.get(id=vacancy_id)
    applications = Application.objects.filter(vacancy_id=vacancy_id)
    vacancy_title = instance.title
    if request.method == 'GET':
        form = VacancyForm(instance=instance)
        context = {
            'form': form,
            'applications': applications,
            'vacancy_title': vacancy_title,
        }
        return render(request, 'vacancy/my_company/my_company_vacancy.html', context=context)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=instance)
        messages.success(request, 'Информация о вакансии обновлена')
        if form.is_valid():
            form.save()
        return redirect('my_company_vacancy', vacancy_id=instance.id)


def profile_view(request: WSGIRequest) -> HttpResponse:
    current_user = request.user
    try:
        company = Company.objects.get(owner_id=current_user)
        return render(request, 'vacancy/profile.html', {'current_user': current_user, 'company': company})
    except Company.DoesNotExist:
        context = {
            'current_user': current_user,
            'company': redirect('company_lets_start')
        }
        return render(request, 'vacancy/profile.html', context=context)


def resume_lets_start_view(request: WSGIRequest) -> HttpResponse:
    return render(request, 'vacancy/my_resume/resume_lets_start.html')


def create_resume_view(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        form = ResumeForm()
    return render(request, 'vacancy/my_resume/create_resume.html', {'form': form})


def my_resume_view(request: WSGIRequest) -> HttpResponse:
    try:
        instance = Resume.objects.get(user=request.user)
        if request.method == 'GET':
            form = ResumeForm(instance=instance)
            return render(request, 'vacancy/my_resume/my_resume.html', {'form': form})
        if request.method == 'POST':
            form = ResumeForm(request.POST, instance=instance)
            messages.success(request, 'Информация о резюме обновлена')
            if form.is_valid():
                form.save()
            return redirect('my_resume')
    except Resume.DoesNotExist:
        return redirect('resume_lets_start')


class SearchView(ListView):
    model = Vacancy
    context_object_name = 'vacancies'
    template_name = 'vacancy/search.html'

    def get_queryset(self):
        query = self.request.GET.get('s')
        if query:
            return Vacancy.objects.filter(title__icontains=query) | Vacancy.objects.filter(skills__icontains=query) \
                   | Vacancy.objects.filter(description__icontains=query)
        else:
            return Vacancy.objects.all()


def custom_handler404(request: WSGIRequest, exception) -> HttpResponse:
    return render(request, 'vacancy/404.html', status=400)


def custom_handler500(request: WSGIRequest) -> HttpResponse:
    return render(request, 'vacancy/500.html', status=500)
