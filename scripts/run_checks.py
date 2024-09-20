"""
This module provides a class to read a data contract, translate it,
prepare a scan, execute the scan, and display the results.
"""

import time
from soda.contracts.data_contract_translator import DataContractTranslator
from soda.scan import Scan


class DataContractScanner:
    """
    A class to read a data contract, translate it, prepare a scan,
    execute the scan, and display the results.
    """
    def __init__(self):
        self.scan = Scan()

    def read_data_contract(self, file_path):
        """
        Read a data contract from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The data contract.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def translate_data_contract(self, data_contract_str):
        """
        Translate a data contract.

        Args:
            data_contract_str (str): The data contract.

        Returns:
            str: The translated data contract.
        """
        data_contract_parser = DataContractTranslator()
        return data_contract_parser.translate_data_contract_yaml_str(data_contract_str)

    def prepare_scan(self, sodacl_str):
        """
        Prepare a scan.

        Args:
            sodacl_str (str): The  Soda Checks Language string.
        """
        data_source_name = "vertica_local"
        result_file_name = f"./data/results/{data_source_name}_results_{time.time()}.json"
        self.scan.set_verbose(True)
        self.scan.set_data_source_name(data_source_name)
        self.scan.add_configuration_yaml_file(file_path="configuration/configuration.yml")
        self.scan.add_sodacl_yaml_str(sodacl_str)
        self.scan.set_scan_results_file(result_file_name)

    def execute_scan(self):
        """
        Execute a scan.

        Returns:
            dict: The scan result.
        """
        return self.scan.execute()

    def display_results(self):
        """
        Display the scan results.
        """
        checks = self.scan.get_scan_results()['checks']
        print(f"check counts: {len(checks)}")
        for check in checks:
            status = check['outcome']
            outcomes = ''
            if status != 'pass':
                outcomes = f" with outcomes: {check['diagnostics']}"
            print(f"{check['name']} with status: {status}{outcomes}")

    def run_checks(self, data_contract_path):
        """
        Run checks on a data contract.

        Args:
            data_contract_path (str): The path to the data contract.
        """
        # Read data contract
        data_contract_str = self.read_data_contract(data_contract_path)

        # Translate data contract
        sodacl_str = self.translate_data_contract(data_contract_str)
        print(sodacl_str)

        # Prepare scan
        self.prepare_scan(sodacl_str)

        # Execute scan
        result = self.execute_scan()
        print(result)

        # Display results
        self.display_results()
        