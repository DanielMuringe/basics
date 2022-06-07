from sqlite3 import connect as sqlite3_connect




class crudTable():
'''
The class allows manipulation af an slqite3 table as a sole entity
'''
    def __init__(self,dbPath):
        with sqlite3_connect(dbPath) as db:
            self.dbCursor = db.cursor()

    class create():
        def table(self,name,fieldList):
            self.dbCursor.execute(f'''CREATE TABLE {name}(  {'?,'*len(fieldList)[:-1]}  );''', fieldList)
        def record(self,)

        
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
    
    