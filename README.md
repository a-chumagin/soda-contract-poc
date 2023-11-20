# Data Contract POC with Soda Core

This project serves as a Proof of Concept (POC) for implementing a data contract using Soda Core. It demonstrates the orchestration and automation of tasks related to data contracts, including connecting to a Vertica database, generating a data contract, and performing checks using Soda SQL.

Why Vertica? because Vertica creates initial data when starting the container, which makes it easier to test the POC.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/soda-contract-poc.git
    cd soda-contract-poc
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Manually start the Vertica container:

    ```bash
    docker-compose -f ./docker/docker-compose.yml up -d
    ```
    If you are using Mac M1 Processor then use the following command to install  Verica container: 
     ```bash
    docker run -p 5433:5433 -p 5444:5444 --name vertica_ce   --platform linux/amd64   --env VERTICA_MEMDEBUG=2 vertica/vertica-ce:12.0.4-0
    ```
## Usage

Run the following command to generate a data contract and perform checks:

```bash
python scripts/main_script.py
```
