from django.shortcuts import render
from . import db


def table(request):
    info_in_table = db.check_info_in_portal_table()
    all_data = []
    for i in info_in_table:
        id_list = i[0]
        company_name_list = i[1]
        person_list = i[2]
        data = {
            'id': id_list,
            'company_name': company_name_list,
            'person': person_list
        }
        all_data.append(data)
        print(data)
    # print(all_data)
    return render(request, 'tablePage.html', all_data)