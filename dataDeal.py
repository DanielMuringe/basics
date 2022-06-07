from sqlite3 import connect as sqlite3_connect




class crudTable():
'''
The class allows manipulation af an slqite3 table as a sole entity
'''
    def __init__(self,dbPath,tableName):
        with sqlite3_connect(dbPath) as db:
            self.dbCursor = db.cursor()
            self.name = tableName
#   Check if table exists to create it.
            self.dbCursor.execute('SELECT ')



    class create():
        def __init__(self,fieldlist):
            self.fieldlist = fieldlist
        def table(self,):
            self.dbCursor.execute(f'''CREATE TABLE IF NOT EXISTS{name}(  {'?,'*len(self.fieldList)[:-1]}  );''', self.fieldList)
        def records(self,):


        
'''
create: 
    tables  
    records  

'''
        pass
    class read():
        pass
    class update():
        pass
    class delete():
        pass

def csvToDb(csvPath,dbTable):
    main = None
    with open(csvPath) as mainFile:
        main = mainFile.readlines()
        main = map(lambda line: line.split(','), main)
        main = map(lambda line: line[-1] = line[-1].replace('\n',''),main)
    
    dbTable.create.records(main)

def table_exists(tablename,connection):
    
    
    