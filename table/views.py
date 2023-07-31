from django.shortcuts import render
from . import db

# Create your views here.
def table(request):
    info_in_table = db.check_info_in_portal_table()
    id_list = []
    company_name_list = []
    person_list = []
    for i in info_in_table:
        id_list.append(i[0])
        company_name_list.append(i[1])
        person_list.append(i[2])
    data = {
        'id': id_list,
        'company_name': company_name_list,
        'person': person_list
    }
    print(data)
    return render(request, 'tablePage.html', data)