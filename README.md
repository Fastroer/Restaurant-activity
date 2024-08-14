
# Restaurant Activity Project

This project is a FastAPI application for managing restaurant opening hours. It provides an API that formats and returns the restaurant's schedule in a human-readable format.

## Project Structure

```
Restaurant-activity/
│   .env                         # Environment configuration file
│   .flake8                      # flake8 configuration file
│   .gitignore                   # Git ignore file
│   docker-compose.yml           # Docker Compose file for running the application
│   Dockerfile                   # Dockerfile for building the Docker image
│   README.md                    # Project documentation
│   requirements.txt             # Project dependencies
│   
├───.github                      # GitHub workflows for CI/CD
│   └───workflows
│           ci.yml               # GitHub Actions CI/CD configuration
│
├───app                          # Application source code
│       config.py                # Application configuration
│       exceptions.py            # Custom exceptions
│       main.py                  # FastAPI application entry point
│       models.py                # Data models (Pydantic)
│       services.py              # Business logic and services
│       utils.py                 # Utility functions
│       __init__.py              # Package initializer
│
└───tests                        # Unit and integration tests
        test_main.py             # Tests for main application
        test_services.py         # Tests for service functions
        test_utils.py            # Tests for utility functions
        __init__.py              # Package initializer for tests
```

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Docker**: Containerization of the application for easy deployment.
- **GitHub Actions**: Continuous Integration and Continuous Deployment (CI/CD).
- **pytest**: Testing framework for writing simple and scalable test cases.
- **flake8**: Tool for checking the style guide enforcement for Python code.

## How to Run the Application

To run the application using Docker, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your machine.

2. Clone the repository:

   ```bash
   git clone https://github.com/Fastroer/Restaurant-activity.git
   cd Restaurant-activity
   ```

3. Before running the application, copy the `.env.example` file to `.env` and edit it according to your environment:

   ```bash
   cp .env.example .env
   ```

4. Build and start the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker image and start the application in a container. The application will be available at `http://localhost:8000`.

5. Access the API documentation:

   Open your browser and go to `http://localhost:8000/api` to view the automatically generated API documentation by FastAPI.

## How to Test the Application

To run tests inside the Docker container, follow these steps:

1. Ensure that the application is running in Docker:

   ```bash
   docker-compose up --build
   ```

2. In another terminal, execute the following command to run tests inside the container:

   ```bash
   docker exec -it restaurant-activity-web-1 pytest tests/
   ```

   This command will run all the tests defined in the `tests/` directory and display the results.

3. To check the code style with flake8:

   ```bash
   docker exec -it restaurant-activity-web-1 flake8 .
   ```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome contributions that improve the project.

## License

This project is licensed under the MIT License.

## Contact information

Author: Ivan Gerasimchik
Email: iv.gerasimchik@gmail.com