# FastAPI Web Application

This project is a web application built using FastAPI, with a PostgreSQL database and Redis caching. It provides a simple API with endpoints to demonstrate basic functionality.

## Project Structure

```
fastapi-web-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── endpoints
│   │   │   ├── __init__.py
│   │   │   ├── hello.py
│   │   │   ├── db_check.py
│   │   │   └── redis_check.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   ├── models
│   │   ├── __init__.py
│   │   └── base.py
│   └── services
│       ├── __init__.py
│       └── redis.py
├── nginx
│   └── default.conf
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── .env
└── README.md
```

## Features

- **Hello World Endpoint**: Returns a simple "Hello World" message.
- **Database Connection Check**: An endpoint to verify the connection to the PostgreSQL database.
- **Redis Connection Check**: An endpoint to verify the connection to Redis.

## Requirements

To run this application, you need to have the following dependencies installed:

- FastAPI
- PostgreSQL
- Redis
- SQLAlchemy
- Alembic

You can install the required packages using:

```
pip install -r requirements.txt
```

## Running the Application

To start the FastAPI application, run the following command:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /hello`: Returns "Hello World".
- `GET /db_health`: Checks the connection to the PostgreSQL database.
- `GET /redis_health`: Checks the connection to Redis.

## Docker Setup

### Dockerfile

This project uses a multi-stage Dockerfile to create a production-ready containerized application. The Dockerfile is structured as follows:

1. **Build Stage**: Installs dependencies and copies application code.
2. **Production Stage**: Creates a lightweight image for running the FastAPI application.
3. **Nginx Stage**: Sets up Nginx as a reverse proxy.

### docker-compose.yml

The `docker-compose.yml` file defines the services for the application, including FastAPI, PostgreSQL, Redis, and Nginx, and their configurations.

## Building and Running the Project

### Using Docker

To build and run the project using Docker, follow these steps:

1. **Build and Start the Docker Containers**:
   Run the following command to build the Docker images and start the containers:
   ```bash
   sudo docker-compose up --build
   ```

## Security Scan Results

To ensure the security of your application, you can perform security scans on your Docker images using tools like **Trivy** or **Docker Scout**. Below are the steps to perform these scans:

### Using Trivy

1. **Install Trivy**:
   Follow the installation instructions for your operating system from the [official Trivy documentation](https://aquasecurity.github.io/trivy/).

2. **Scan a Docker Image**:
   Run the following command to scan your Docker image:
   ```bash
   trivy image <image_name>



