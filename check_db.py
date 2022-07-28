import psycopg2

def add_db(links):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="boolax45",
                                    host="mtg-db.cbailyzpcsf3.us-east-1.rds.amazonaws.com",
                                    port="5432",
                                    database="postgres")
        
        cursor = connection.cursor()
        for link in links:
            postgres_insert_query = """ INSERT INTO pics (link) VALUES (%s)"""
            record_to_insert = (link,)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#add_db('hjsdhfjshdf')

def in_db(link):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="boolax45",
                                    host="mtg-db.cbailyzpcsf3.us-east-1.rds.amazonaws.com",
                                    port="5432",
                                    database="postgres")
        
        cursor = connection.cursor()
        #for link in links:
            #print(link)
        sql = "SELECT * FROM pics WHERE link = '{}' ;".format(link)
        #record_to_query = (links)
        cursor.execute(sql)
        one = cursor.fetchone()
        #print(links)
        if one:
            return True
            #connection.commit()
            #count = cursor.rowcount
            #print(count, "Record inserted successfully into mobile table")

    #except (Exception, psycopg2.Error) as error:
        #print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")