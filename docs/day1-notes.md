# Day 1 Notes

## 1. What is FastAPI?

FastAPI is a modern, fast web framework for building APIs with Python. It is designed for high performance, easy development, and automatic generation of interactive API documentation.

## 2. Why did we choose FastAPI instead of Django?

FastAPI is chosen for backend APIs because it is lightweight, faster to start with, and focused on building RESTful services. Django is a larger framework that includes many built-in features for web applications, while FastAPI is better suited for small-to-medium API-first projects and modern async workflows.

## 3. What is ASGI?

ASGI stands for Asynchronous Server Gateway Interface. It is a specification that allows Python web applications to handle asynchronous communication, making it possible to support long-lived connections, websockets, and high-concurrency API requests.

## 4. What is Uvicorn?

Uvicorn is a fast ASGI server implementation for Python. It runs ASGI applications and serves the application to clients, handling asynchronous request processing efficiently.

## 5. What is a virtual environment?

A virtual environment is an isolated Python environment that keeps project-specific dependencies separate from the system Python installation. It ensures the project uses consistent package versions and avoids conflicts with other projects.

## 6. What is an API endpoint?

An API endpoint is a URL path where a client can send a request to interact with the backend service. Each endpoint corresponds to a specific action or resource, such as fetching data or updating a record.

## 7. What is Swagger UI?

Swagger UI is an interactive web interface for exploring and testing APIs. FastAPI automatically generates Swagger UI documentation so developers can see available endpoints, request parameters, and response schemas.
