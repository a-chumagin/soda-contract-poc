# Data Contract POC with Soda Core

This project serves as a Proof of Concept (POC) for implementing a data contract using Soda Core. It demonstrates the orchestration and automation of tasks related to data contracts, including connecting to a Vertica database, generating a data contract, and performing checks using Soda SQL.

Why Vertica? Because Vertica creates initial data when starting the container, which makes it easier to test the POC.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/soda-contract-poc.git
    cd soda-contract-poc
    ```

## Usage
Run the Docker Compose file to start the Vertica container and the Soda Check container:

    ```bash
    docker-compose -f ./docker/docker-compose.yml up
    ```

If you are using a Mac M Processor, use the following command to run the Vertica container:

    ```bash
    export DOCKER_DEFAULT_PLATFORM=linux/arm64
    export DOCKER_BUILDKIT=0
    docker-compose -f ./docker/docker-compose.yml up
    ```

## Reports
### Viewing Reports
The reports are created using Streamlit and visualize the results from Soda scans. Once the reports service is running, you can access the reports at:
```
http://0.0.0.0:8501
```

### Report Components 
The reports include the following components:

- **Summary**: An overview of the scan results, including the definition name, default data source, and the time taken for the scan.
- **Checks**: Detailed information about each check, including:
    - **Name**: The name of the check.
    - **Table name**: The table associated with the check.
    - **Outcome**: The result of the check (pass or fail).
    - **Diagnostics**: Diagnostic information related to the check.
    - **Description**: A description of the check.
- **Passed Checks**: A table listing all the checks that passed.
- **Failed Checks**: A table listing all the checks that failed.
- **Logs**: Logs generated during the scan.

### Select Report:
You can select particular reports from selectbox. Just choose file name for rendering in reports 

### Sharing Reports
Streamlit provides an option to share the report link. You can use the share link to share the report with others.

The link to the report is:
```
http://localhost:8501/?file=vertica_local_results_1726854394.0941107.json