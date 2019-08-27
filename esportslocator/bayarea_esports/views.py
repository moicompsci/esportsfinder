from django.shortcuts import render
#import psycopg2 module to communicate with PostgreSQL
import psycopg2
#The Error class handles any db error/exception that can occur
#Need this to make our application robust
from psycopg2 import Error
import pandas as pd
import pandas.io.sql as psql

#my credentials: dbname, user, password
from bayarea_esports.creds import con_str

#Selects all rows from our table in our database and returns it as a dictionary
def load_data(schema, table):
    connection = None
    try:
        connection = psycopg2.connect(con_str)
        cursor = connection.cursor()
        sql_cmd = 'SELECT * FROM {}.{}'.format(str(schema), str(table))
        data = pd.read_sql(sql_cmd, connection)

        
        #return a dictionary 
        return data.to_dict('records')
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error executing query: ', error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print('Connection now closed')



def home(request):

    data = load_data('public', 'bay_area_smash_esports')
    print('data ', data)
    context = {
                'posts':data
            }

    #We want the user to see that header when they go to our home page
    #render function still returns an HTTP response in the background
    #will always return and HTTP response or an exception
    #returns a rendered template instead of an HTTP Resonse
    #render takes the request as it's first argument
    #2nd arguement path to our html template
    return render(request, 'bayarea_esports/home.html', context)


def about(request):
    return render(request, 'bayarea_esports/about.html')

