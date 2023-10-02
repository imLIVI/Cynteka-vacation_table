import psycopg2

def query_execute(cursor):   
    query = "select integration_vacation.id, company.short_name, company.cynteka_address, person.last_name " +  "from integration_vacation " + "left join company on integration_vacation.company_id = company.id " + "left join person on integration_vacation.manager_id = person.id"
    cursor.execute(query)

    # Получение строк запроса
    query_res = cursor.fetchall()

    return query_res

def connect():
    # Подключение к порталу
    connection = psycopg2.connect(
        dbname="cyfoman", 
        host="172.16.50.20", 
        user="lipatnikova", 
        password="J832s357", 
        port="5432")
    
    with connection:
        with connection.cursor() as cursor:
            print("Connection to Zakupay is success")
    
    # Получаем объект для выполнения запрососв к БД
    cursor = connection.cursor()
        
    # Для того, чтобы query автоматически выполнялись при вызове метода cursor.execute()
    connection.autocommit = True

    return cursor, connection


# Закрытие подключения
def close(cursor, connection):
    cursor.close()
    connection.close()



