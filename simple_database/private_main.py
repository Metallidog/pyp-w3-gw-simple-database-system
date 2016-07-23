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
    Returns a Database object with acess to the directory
    Raises an Error if file already exists
    """
    db_dir_path = BASE_DB_FILE_PATH + db_name +'/'
    if os.path.exists(db_dir_path):
        raise ValidationError("already exists")
    else:
        os.makedirs(db_dir_path)
        return Database(db_name)
            
def connect_database(db_name):
    raise NotImplementedError()

class Database(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.table_names = []
        
    def create_table(self, table_name, columns = []):
        table_path = BASE_DB_FILE_PATH + self.file_name + '/' + table_name
        if os.path.exists(table_path):
        	raise ValidationError("already exists")
        else:
        	#columns.insert(0, {'config': table_name})
        	self.table_names.append(table_name)
        	return Table(
        	with open(table_path, 'wb') as table:
        		pickle.dump(columns, table)
        		
    def show_tables(self):
    	return self.table_names
    	
class Table(object):
	def __init__(self, table_name, table_path):
		
		
		
if __name__ == '__main__':
    if os.path.exists(BASE_DB_FILE_PATH):
        shutil.rmtree(BASE_DB_FILE_PATH)
    db = create_database('first')
    db.create_table('authors', columns=[
            {'name': 'id', 'type': 'int'},
            {'name': 'name', 'type': 'str'},
            {'name': 'birth_date', 'type': 'date'},
            {'name': 'nationality', 'type': 'str'},
            {'name': 'alive', 'type': 'bool'},
             ])
    f = open('/tmp/simple_database/first/authors', 'rb')
    data = pickle.load(f)
    print (data)
    print (db.show_tables())