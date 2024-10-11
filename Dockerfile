# Use the official Python image.
FROM python:3.10-slim

RUN apt-get update \
    && apt-get -y install build-essential

# Set the working directory in the container
WORKDIR /

# Copy requirements.txt
COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory
COPY ./app /app
COPY ./tests /tests

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]