"""
This module provides a function to generate a data contract from column information.
The data contract is a YAML representation of the dataset and its columns.
"""

import re
import yaml


def generate_data_contract(column_info):
    """
    Generate a data contract from column information.

    Args:
        column_info (dict): A dictionary that includes 
        the table name and a list of columns.
            Each column is represented as a tuple that 
            includes the column name, data type, and a nullable flag.

    Returns:
        str: A string representation of the data contract in YAML format.
    """
    data_contract = {
        'dataset': column_info['table_name'],
        'columns': [],
    }

    for column in column_info['columns']:
        column_name, data_type, is_nullable = column
        column_data = {
            'name': column_name,
            'data_type': data_type,
            'not_null': not is_nullable
        }

        data_contract['columns'].append(column_data)

    return yaml.dump(data_contract, default_flow_style=False)
