import psycopg2

def connection_portal():
    connect = None
    try:
        connect = psycopg2.connect(
            host="172.16.50.20",
            port="5432",
            dbname="cyfoman",
            user="goncharov",
            password="HelloBase3649")

        cursor = connect.cursor()
        cursor.close()
        return connect
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, "Error")



def check_info_in_portal_table():
    try:
        connect_portal = connection_portal()
        cursor_portal = connect_portal.cursor()
        select = ("select integration_vacation.id, company.short_name, person.last_name "
                  "from integration_vacation left join company on integration_vacation.company_id = company.id "
                  "left join person on integration_vacation.manager_id = person.id")
        cursor_portal.execute(select)
        information = cursor_portal.fetchall()
        # print(information)
        cursor_portal.close()
        connect_portal.close()
        return information
    except Exception as error:
        print("check_info_in_portal_table " + str(error))