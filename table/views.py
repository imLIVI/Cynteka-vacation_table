from django.shortcuts import render
from . import database

# Функция для получения статуса компании (ALIVE) в
def get_bool_company_status(str_status):
    if str_status == 'True':
            status = True
    else: 
        status = False

    return status


# Парсинг запроса для формирования списка словарей
def query_main_parse(info_list):
    dict_list = []

    for info in info_list:

        dict = {
        'id': info[0],
        'status' : get_bool_company_status(info[1]),
        'company': info[2],
        'person': info[3]
        }
        dict_list.append(dict)
    return dict_list

# Парсинг запроса для формирования списка внедренцев
def query_persons_parse(persons_list):
    person_list = []

    for person in persons_list:
        person_list.append(person[0])
    
    return person_list

def get_context(dict_list, person_list):
    return {'dict_list' : dict_list,
            'person_list' : person_list}  

# Create your views here.
def table(request):
    cursor, connection = database.connect()

    # Основной запрос для таблицы
    query_main = ("select integration_vacation.id, "
    "CASE "
       "WHEN company.cynteka_status = 'ALIVE' THEN 'True' "
        "ELSE 'False' "
    "END as company_status, "
    "company.cynteka_address, "
    "CONCAT(person.last_name, ' ',  person.first_name)"
    "from integration_vacation "
    "left join company on integration_vacation.company_id = company.id "
    "left join person on integration_vacation.manager_id = person.id ")
    res_query = database.query_execute(cursor, query_main)
    print(res_query)
    dict_list = query_main_parse(res_query)


    # Запрос для получения списка внедренцев
    query_get_person = ("select DISTINCT(CONCAT(person.last_name, ' ',  person.first_name)) "
        "from integration_vacation "
        "left join company on integration_vacation.company_id = company.id "
        "left join person on integration_vacation.manager_id = person.id")
    res_query = database.query_execute(cursor, query_get_person)
    print(res_query)
    person_list = query_persons_parse(res_query)

    # Создание словаря (context) для html
    dict_list = get_context(dict_list, person_list)

    database.close(cursor, connection)
   
    

    #TODO: вместо {} должен передаваться словарь: context: persons
    return render(request, 'tablePage.html', context=dict_list)
