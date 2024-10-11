# FastAPI Caching Service

This is a FastAPI microservice that provides caching capabilities for generated payloads. It features endpoints to create and read payloads using lists of strings and a transformer function.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Using the Linter](#using-the-linter)

## Project Overview

The service provides the following functionalities:

- Create a payload by sending two lists of strings.
- Retrieve the generated payload using its unique identifier.
- Cache the generated results for reuse to improve performance.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
```bash
   git clone https://github.com/allrested/FastAPI_Caching_Services.git
   cd FastAPI_Caching_Services
```
2. **Compose Docker Container**:
```bash
   docker compose up -d
```

## Running the Application

You can then access the application at http://localhost.

## API Endpoints

### Create Payload

**POST** /payload

**Request Body**:
```json
{
  "list_1": ["first string", "second string", "third string"],
  "list_2": ["other string", "another string", "last string"]
}
```

**Response**:
```json
{
  "message": "Payload Generated",
  "id": "unique_payload_id"
}
```

### Read Payload

**GET** /payload/{id}

**Response**:
```json
{
  "output": "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"
}
```

## Running Tests

To run the test suite for this application, you can use `pytest`. Run the tests with the following command:
```bash
   pytest /tests/
```

You can also use the Makefile to run tests:
```bash
   make test
```

## Using the Linter

This project uses `flake8` and `black` for code linting and formatting. To lint the code, you can run:
```bash
   make lint
```
To format the code with `black`, use:
```bash
   make format
```
