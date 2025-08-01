# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app  # Simpler: Use /app as the working directory

# Copy the entire project into the container
COPY . /app

# Change current directory to src for installation and execution
WORKDIR /app/src

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Disables the cache, which is not needed in a container build and saves space.
# --upgrade pip: Ensures we have the latest version of pip.
RUN pip install --no-cache-dir --upgrade pip -r /app/requirements.txt

# Create the logs directory
RUN mkdir -p /app/src/logs

# Run the Python script using its path.  This is much simpler and less error-prone.
CMD ["python", "main.py"] # Or: CMD ["python", "/app/src/main.py"]