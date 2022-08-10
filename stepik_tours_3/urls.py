"""stepik_tours_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from vacancy.views import company_view, main_view, specialty_view, vacancies_view, vacancy_view, custom_handler404, \
    custom_handler500

handler400 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
                  path('', main_view, name='main'),
                  path('vacancies/', vacancies_view, name='vacancies'),
                  path('vacancies/cat/<str:specialty>/', specialty_view, name='specialty'),
                  path('companies/<int:company_id>/', company_view, name='company'),
                  path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
