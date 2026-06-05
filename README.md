# Dockerized System Monitor

A beginner-friendly DevOps project that demonstrates how to containerize a Python Flask application using Docker.

The application exposes:

* `/` – Main application page
* `/health` – Health check endpoint

This project is part of a Cloud & DevOps hands-on learning portfolio focused on Docker fundamentals, containerization, and application deployment.

---

## Project Structure

```text
Dockerized-System-Monitor/
│
├── .gitignore
├── README.md
├── docker-compose.yml
│
├── app/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── db/
│   └── .gitkeep
│
└── screenshots/
    ├── Docker_Image.png
    ├── Docker_Output-1.png
    ├── Docker_Output-2.png
    ├── Docker_Ps-Logs.png
    ├── Docker_Run.png
    └── Dokcer_Build.png
```

---

## Technologies Used

* Python 3.12
* Flask
* Docker
* Docker Compose
* Linux (Ubuntu WSL2)

---

## Features

* Python Flask web application
* Dockerized application deployment
* Custom Docker image creation
* Container lifecycle management
* Health check endpoint
* Docker build and run workflow
* GitHub portfolio-ready documentation

---

## Application Endpoints

### Home Page

```http
GET /
```

Returns the main application page.

### Health Check

```http
GET /health
```

Returns application health status.

Example:

```json
{
  "status": "healthy"
}
```

---

## Dockerfile Concepts Demonstrated

### COPY

Copies application files into the Docker image.

```dockerfile
COPY . .
```

### EXPOSE

Documents the application port used by the container.

```dockerfile
EXPOSE 5000
```

### CMD

Defines the default command executed when the container starts.

```dockerfile
CMD ["python", "app.py"]
```

---

## Build Docker Image

Navigate to the project root directory:

```bash
cd Dockerized-System-Monitor
```

Build the image:

```bash
docker build -t dockerized-system-monitor ./app
```

---

## Verify Image

```bash
docker images
```

---

## Run Container

```bash
docker run -d \
-p 5000:5000 \
--name monitor-app \
dockerized-system-monitor
```

---

## Verify Running Container

```bash
docker ps
```

---

## View Container Logs

```bash
docker logs monitor-app
```

---

## Access Application

Home Page:

```text
http://localhost:5000
```

Health Endpoint:

```text
http://localhost:5000/health
```

---

## Screenshots

### Docker Build

![Docker Build](screenshots/Dokcer_Build.png)

### Docker Image

![Docker Image](screenshots/Docker_Image.png)

### Docker Run

![Docker Run](screenshots/Docker_Run.png)

### Docker PS and Logs

![Docker PS and Logs](screenshots/Docker_Ps-Logs.png)

### Application Output (/)

![Application Output](screenshots/Docker_Output-1.png)

### Health Endpoint (/health)

![Health Endpoint](screenshots/Docker_Output-2.png)

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Creating Docker images
* Building custom Dockerfiles
* Running and managing containers
* Port mapping
* Flask application deployment
* Docker troubleshooting
* Linux command-line operations
* Git and GitHub project management

---

## Future Enhancements

* Add MySQL database integration
* Implement Docker Compose multi-container deployment
* Add persistent storage using volumes
* Add environment variable management
* Deploy on AWS EC2
* Implement CI/CD using GitHub Actions

---

## Author

Kashyap Kurani

Cloud & DevOps Learning Portfolio Project

