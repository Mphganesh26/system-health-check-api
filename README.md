System Health Check API
Overview

This project implements a Python-based FastAPI application that evaluates the health of a system composed of multiple interdependent components arranged as a Directed Acyclic Graph (DAG).

The application:

    Builds a DAG from input data
    Traverses the graph using Breadth First Search (BFS)
    Performs asynchronous health checks on components
    Aggregates component health results
    Exposes REST APIs using FastAPI
    Provides Swagger/OpenAPI documentation

Technologies Used
    Python 3.x,
    FastAPI,
    Asyncio,
    Pytest,
    Docker,
    Terraform,
    GitHub Actions

Core Features
    DAG construction from JSON input, 
    Breadth First Search (BFS) traversal, 
    Asynchronous component health evaluation, 
    Health result aggregation, 
    FastAPI REST API

Additional Features
    Swagger/OpenAPI documentation,
    Structured logging,
    Unit testing using Pytest

API Endpoints
    GET /

    Returns application status.

    Example Response:

    {
    "message": "System Health Check API is running"
    }

POST /health-check
    Accepts component dependency information and returns component health results.

Assumptions
    Input graph is a valid DAG.
    Component identifiers are unique.
    Health checks are independent.
    Health status is simulated for demonstration purposes.

Design Decisions
DAG Modeling

    A Directed Acyclic Graph was chosen because system dependencies naturally form a dependency hierarchy.

BFS Traversal

    BFS was selected because it was explicitly required in the assignment and allows level-by-level traversal of dependent components.

Async Health Checks

    Async processing allows multiple component health checks to execute concurrently, improving scalability.

FastAPI

    FastAPI was chosen because it provides:
        High performance
        Built-in Swagger documentation
        Easy request validation
        Async support


Observability
    The application includes basic observability features:

Logging

    Application events are logged using Python logging.

    Examples:

    Health check request received
    BFS traversal order generated
    Health check completed


Health Endpoint
    Root endpoint can be used as a simple service availability check.

API Documentation
    Swagger UI provides visibility into API contracts and request/response structures.

Running Locally
    Install Dependencies
        pip install fastapi uvicorn pytest
    Run Application
        uvicorn app.main:app --reload
    Run Tests
        python -m pytest


API Documentation

    After starting the application, open:

    http://127.0.0.1:8000/docs

    Swagger UI allows testing endpoints directly from the browser.

Sample Request
        {
        "components": [
            {
            "id": "Step1",
            "dependencies": []
            },
            {
            "id": "Step2",
            "dependencies": ["Step1"]
            },
            {
            "id": "Step3",
            "dependencies": ["Step2"]
            }
        ]
        }

Sample Response
        {
        "bfs_order": [
            "Step1",
            "Step2",
            "Step3"
        ],
        "total_components": 3,
        "results": [
            {
            "component": "Step1",
            "status": "HEALTHY"
            },
            {
            "component": "Step2",
            "status": "UNHEALTHY"
            },
            {
            "component": "Step3",
            "status": "HEALTHY"
            }
        ]
        }

Testing

    Unit tests are implemented using Pytest.

    Current test coverage includes:

        BFS traversal validation
        DAG traversal behavior

    Execute tests using:
        python -m pytest


Future Enhancements

The following features were considered but not implemented due to scope limitations:

    DAG visualization with Graphviz
    Metrics collection using Prometheus
    Distributed tracing with OpenTelemetry
    Persistent storage for health results
    Advanced health evaluation logic

Infrastructure as Code
    Terraform configuration is included to demonstrate infrastructure provisioning and deployment automation.

CI/CD

GitHub Actions workflow is included to:
    Install dependencies
    Execute unit tests
    Validate code before deployment

AI Usage

AI assistance was used for:
    Solution design guidance
    FastAPI implementation support
    Unit testing support
    Documentation generation
    Troubleshooting and debugging assistance

All generated code was reviewed, tested, and validated before inclusion in the final solution.

Tradeoffs
Included
    DAG construction
    BFS traversal
    Async processing
    API implementation
    Logging
    Unit testing
Excluded
    Production-grade monitoring stack
    Persistent database storage
    Complex deployment infrastructure

These items were excluded to maintain focus on the core assignment requirements while delivering a complete and maintainable solution.
