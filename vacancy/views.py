from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import render

from vacancy.models import Company, Specialty, Vacancy


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

    context = {
        'vacancy': current_vacancy,
        'company': current_vacancy.company
    }
    return render(request, 'vacancy/vacancy.html', context=context)


def custom_handler404(request: WSGIRequest, exception) -> HttpResponse:
    return render(request, 'vacancy/404.html', status=400)


def custom_handler500(request: WSGIRequest) -> HttpResponse:
    return render(request, 'vacancy/500.html', status=500)
