"""
This module provides the main function to generate a data contract YAML file
from a Vertica table and run checks on the generated file.
"""

from db_operations import (read_vertica_connection_config,
                            create_vertica_connection,
                            get_vertica_table_structure)
from data_contract_generator import generate_data_contract
from run_checks import DataContractScanner


def main():
    """
    The main function to generate a data contract YAML file from a Vertica table
    and run checks on the generated file.
    """
    table_name = 'customer_dimension'
    config_path = 'configuration/configuration.yml'
    data_contract_path = f"data/{table_name}_data_contract.yml"

    vertica_config = read_vertica_connection_config(config_path)

    # Create a Vertica connection
    connection = create_vertica_connection(vertica_config)
    print("Successfully connected to Vertica!")

    column_info = get_vertica_table_structure(table_name, connection)
    data_contract_yaml = generate_data_contract(column_info)

    with open(data_contract_path, 'w', encoding='utf-8') as yaml_file:
        yaml_file.write(data_contract_yaml)

    print("Data contract YAML file generated successfully.")
    scanner = DataContractScanner()
    scanner.run_checks(data_contract_path)


if __name__ == "__main__":
    main()
