FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and set permissions
RUN useradd -r -u 1001 soda-user && \
    mkdir ./data/ && \
    chown soda-user ./data/

# Switch to the soda-user
USER soda-user

# Copy the rest of the application code into the container
COPY ../configuration /app/configuration
COPY ../scripts/*.py /app/

# Set the command to run the application
CMD ["python", "-u", "main_script.py"]
