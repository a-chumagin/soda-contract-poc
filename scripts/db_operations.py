import vertica_python
import yaml
import time
import os

def read_vertica_connection_config(config_path):
    with open(config_path, 'r') as config_file:
        config_data = yaml.safe_load(config_file)
        vertica_config = config_data.get('data_source vertica_local', {}).get('connection')
    return vertica_config

def create_vertica_connection(config, max_retries=3):
    conn_info = {
        'host': os.environ.get('vertica_host', config.get('host')),
        'port': config.get('port'),
        'user': config.get('username'),
        'password': config.get('password'),
        'database': config.get('database'),
        'schema': config.get('schema'),
        'ssl': False  # Set to True if using SSL
    }

    for i in range(max_retries):
        print(conn_info['host'])
        try:
            connection = vertica_python.connect(**conn_info)
            return connection
        except vertica_python.errors.ConnectionError:
            if i < max_retries - 1:
                time.sleep(5)
                continue
            else:
                raise

def get_vertica_table_structure(table_name, connection):
    with connection as conn:
        query = f"SELECT column_name, data_type, is_nullable FROM columns WHERE table_name='{table_name}'"
        conn.cursor().execute(query)
        table_structure = conn.cursor().fetchall()

    return {'table_name': table_name, 'columns': table_structure}
