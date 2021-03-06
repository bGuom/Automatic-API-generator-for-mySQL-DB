import MySQLdb

def scan(dbname,dbhost,dbuser,dbpw):
    tables =[]
    tablecolumns =[]
    tableprimary=[]
    
    try:
        connection = MySQLdb.connect(
                        host = dbhost,
                        user = dbuser,
                        passwd = dbpw) 

        cursor = connection.cursor()   


        cursor.execute("USE "+dbname) 
        cursor.execute("SHOW TABLES")
        
        for (table_name,) in cursor:            
            tables.append(table_name)

        for table in tables:
            cursor.execute("SHOW columns FROM "+table)
            tablecolumns.append([column[0] for column in cursor.fetchall()])
            q = "SELECT COLUMN_NAME FROM information_schema.KEY_COLUMN_USAGE WHERE TABLE_NAME = \'" + table + "\' AND CONSTRAINT_NAME = 'PRIMARY'"
            cursor.execute(q)
            tableprimary.append([column[0] for column in cursor.fetchall()])

        return tables,tablecolumns,tableprimary
        
    except:
        print "Error occured when connecting to db.."
        raw_input('Please try again')
        exit()

#print scan('db_store','localhost','root','')[1]
