"""
This module provides functions to read Vertica connection configuration,
create a Vertica connection, and get the structure of a Vertica table.
"""

import os
import time
import vertica_python
import yaml


def read_vertica_connection_config(config_path):
    """
    Read Vertica connection configuration from a YAML file.

    Args:
        config_path (str): The path to the configuration file.

    Returns:
        dict: The Vertica connection configuration.
    """
    with open(config_path, 'r', encoding='utf-8') as config_file:
        config_data = yaml.safe_load(config_file)
        vertica_config = config_data.get('data_source vertica_local', {}).get('connection')
    return vertica_config


def create_vertica_connection(config, max_retries=3):
    """
    Create a Vertica connection using the provided configuration.

    Args:
        config (dict): The Vertica connection configuration.
        max_retries (int): The maximum number of connection attempts.

    Returns:
        vertica_python.connect: The Vertica connection.
    """
    conn_info = {
        'host': os.environ.get('vertica_host', config.get('host')),
        'port': os.environ.get('port',config.get('port')),
        'user': os.environ.get('vertica_user',config.get('username')),
        'password': os.environ.get('vertica_password',config.get('password')),
        'database': os.environ.get('vertica_db',config.get('database')),
        'schema': os.environ.get('vertica_schema',config.get('schema')),
        'ssl': False  # Set to True if using SSL
    }
    for i in range(max_retries):
        print(conn_info['host'])
        try:
            return vertica_python.connect(**conn_info)
        except vertica_python.errors.ConnectionError:
            if i < max_retries - 1:
                time.sleep(5)
                continue
            raise


def get_vertica_table_structure(schema_name, table_name, connection):
    """
    Get the structure of a Vertica table.

    Args:
        table_name (str): The name of the table.
        connection (vertica_python.connect): The Vertica connection.

    Returns:
        dict: The table structure.
    """
    with connection as conn:
        query = (
            "SELECT c.column_name, t.type_name, c.is_nullable "
            f"FROM columns c JOIN types t ON c.data_type_id = t.type_id "
            f"WHERE table_name='{table_name}' and table_schema='{schema_name}'"
        )

        conn.cursor().execute(query)
        table_structure = conn.cursor().fetchall()

    return {'table_name': table_name, 'columns': table_structure}
