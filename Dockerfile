# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Disables the cache, which is not needed in a container build and saves space.
# --upgrade pip: Ensures we have the latest version of pip.
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# Copy the application source code into the container
COPY ./src /code/src

# Create a directory for logs, as specified in main.py
RUN mkdir logs

# Set the entrypoint to run the Python script.
# Using -m ensures the script is run as a module within the 'src' package,
# which is best practice for packaged applications.
ENTRYPOINT ["python", "-m", "src.main"]