from django.http.response import JsonResponse, Http404
from main.models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.short_jsn() for company in companies]
    return JsonResponse(companies_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.full_jsn())

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.short_jsn() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request , vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.full_jsn())

def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = company.vacancy_set.all()
    vacancies_json = [vacancy.full_jsn() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)




def vacancy_top(request):
    vacancies = Vacancy.objects.filter().order_by("-salary")[:10]
    vacancies_json = [vacancy.short_jsn() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)