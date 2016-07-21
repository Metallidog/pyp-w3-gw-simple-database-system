import os, errno

class ValidationError(Exception):
    pass

BASE_DB_FILE_PATH = '/tmp/simple_database/'


def create_database(db_name):
    db_file_name = BASE_DB_FILE_PATH + db_name
    if os.path.exists(db_file_name):
        raise ValidationError("already exists")
    else:
        os.mkdir(BASE_DB_FILE_PATH)
        with open(db_file_name, 'w+') as f:
            print "We opened the file"
    def create_table(*args, **kwargs):
        print args
        print kwargs
            
    
def connect_database(db_name):
    raise NotImplementedError()


if __name__ == '__main__':
    create_database('first')