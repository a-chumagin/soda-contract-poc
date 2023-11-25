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
    docker-compose -f ./docker/docker-compose.yml up -d
    ```

If you are using a Mac M Processor, use the following command to run the Vertica container:

    ```bash
    export DOCKER_DEFAULT_PLATFORM=linux/arm64
    export DOCKER_BUILDKIT=0
    docker-compose -f ./docker/docker-compose.yml up -d
    ```