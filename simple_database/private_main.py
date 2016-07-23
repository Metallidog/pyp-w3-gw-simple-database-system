import os, errno
#from exceptions import ValidationError
import os
import shutil
import pickle
import json
BASE_DB_FILE_PATH = '/tmp/simple_database/'


def create_database(db_name):
    """
    Creates a directory [db_name] under the BASE_DB_FILE_PATH
    Creates a file in that directory called [db_name].db
    Returns an empty databse
    Raises an Error if file already exists
    """
    db_dir_path = BASE_DB_FILE_PATH + db_name +'/'
    if os.path.exists(db_dir_path):
        raise ValidationError("already exists")
    else:
        os.makedirs(db_dir_path)
        return NewDatabase(db_name, db_dir_path)
            
def connect_database(db_name):
    raise NotImplementedError()

class NewDatabase(object):
    def __init__(self, db_name, db_path):
        db_file = BASE_DB_FILE_PATH + db_name + '/' + db_name + '.db'
        if os.path.exists(db_file):
        	raise ValidationError("DB already exists")
        else:
            self.name = db_name
            self.path = db_path
            self.table_names = []
            init_data = [self.name, self.path, self.table_names]
        with open(db_file, 'wb') as db:
        		pickle.dump(init_data, db)        
        
    def create_table(self, table_name, columns = []):
        table_file = BASE_DB_FILE_PATH + self.name + '/' + table_name+".tb"        
        if os.path.exists(table_file):
        	raise ValidationError("Table already exists")
        else:
        	schema = {'schema': columns}
        	with open(table_file, 'wb') as table:
        		pickle.dump(schema, table)
        		
    def show_tables(self):
    	return self.table_names
    	
class Table(object):
	def __init__(self, table_name, table_path):
		self.name = table_name
		self.path = table_path		
		
if __name__ == '__main__':
    #if os.path.exists(BASE_DB_FILE_PATH):
        #shutil.rmtree(BASE_DB_FILE_PATH)
    db = create_database('home')
    db.create_table('authors', columns=[
            {'name': 'id', 'type': 'int'},
            {'name': 'name', 'type': 'str'},
            {'name': 'birth_date', 'type': 'date'},
            {'name': 'nationality', 'type': 'str'},
            {'name': 'alive', 'type': 'bool'},
             ])
  