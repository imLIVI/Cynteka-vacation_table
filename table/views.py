from django.shortcuts import render
from . import database

# Create your views here.
def table(request):
    cursor, connection = database.connect()
    res_query = database.query_execute(cursor)
    print(res_query)

    database.close(cursor, connection)
    return render(request, 'tablePage.html', {})

