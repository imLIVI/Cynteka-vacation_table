from django.shortcuts import render
from . import database

# Парсинг запроса для формирования списка словарей
def query_parse(persons_list):
    dict_list = []
    for person_info in persons_list:
        dict = {
        'id': person_info[0],
        'company_name': person_info[1],
        'company_site': person_info[2],
        'person': person_info[3]
        }
        dict_list.append(dict)
    return dict_list  

def get_context(dict_list):
    return {'dict_list' : dict_list}

# Create your views here.
def table(request):
    cursor, connection = database.connect()
    res_query = database.query_execute(cursor)
    #query_parse(res_query)

    #print(res_query)

    database.close(cursor, connection)
    dict_list = get_context(query_parse(res_query))

    #TODO: вместо {} должен передаваться словарь: context: persons
    return render(request, 'tablePage.html', context=dict_list)
