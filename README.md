# End-to-End DevOps Automation Platform

A Python-based system monitoring platform that demonstrates containerization, automated testing, CI/CD, and infrastructure monitoring using Docker, GitHub Actions, Prometheus, and Grafana.

## Project Overview

This project collects system CPU, memory, and disk usage metrics and exposes them through a Prometheus-compatible endpoint. Prometheus scrapes the metrics, while Grafana visualizes them in dashboards.

The project also uses GitHub Actions to automate Python testing and Docker image building, with a separate workflow for publishing the image to GitHub Container Registry (GHCR).

## Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI/CD
    |
    +--> Run Python Tests
    |
    +--> Build Docker Image
    |
    +--> Publish Image to GHCR
    |
    v
Docker Compose
    |
    +--> Python Metrics Exporter :8000
    |
    +--> Prometheus              :9090
    |         |
    |         v
    +------> Grafana              :3000
```

## Technology Stack

- **Programming:** Python
- **Monitoring:** Prometheus, Grafana
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Testing:** pytest
- **Metrics:** psutil, prometheus-client
- **Version Control:** Git and GitHub
- **Operating System:** Ubuntu Linux

## Features

- Collects CPU utilization metrics.
- Collects memory utilization metrics.
- Collects disk utilization metrics.
- Exposes metrics through an HTTP endpoint.
- Scrapes application metrics using Prometheus.
- Visualizes monitoring data using Grafana.
- Runs automated Python tests through GitHub Actions.
- Builds Docker images automatically.
- Publishes Docker images to GitHub Container Registry.

## Project Structure

```text
devops-automation-platform/
├── app/
│   ├── monitor.py
│   └── metrics_server.py
├── tests/
│   └── test_monitor.py
├── monitoring/
│   └── prometheus.yml
├── docker/
├── scripts/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── docker-publish.yml
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Ubuntu or another Linux distribution
- Python 3.10 or compatible
- Git
- Docker
- Docker Compose

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Pavankumar-20/devops-automation-platform.git
cd devops-automation-platform
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest -v
```

## Start the Monitoring Stack

Build and start the services:

```bash
sudo docker compose up -d --build
```

Check container status:

```bash
sudo docker compose ps
```

View application logs:

```bash
sudo docker compose logs --tail=50 app
```

## Access the Services

| Service | URL |
|---|---|
| Application metrics | http://localhost:8000/metrics |
| Prometheus | http://localhost:9090 |
| Prometheus targets | http://localhost:9090/targets |
| Grafana | http://localhost:3000 |

Configure Grafana to use the Prometheus data source URL `http://prometheus:9090` when Grafana is running in the same Docker Compose network.

## Prometheus Queries

CPU usage:

```promql
system_cpu_usage_percent
```

Memory usage:

```promql
system_memory_usage_percent
```

Disk usage:

```promql
system_disk_usage_percent
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. Checks out the source code.
2. Sets up Python.
3. Installs dependencies.
4. Runs pytest tests.
5. Builds a Docker image.

The Docker publishing workflow builds and publishes the image to GHCR when triggered by a push to the `main` branch.

## Docker Image

```text
ghcr.io/pavankumar-20/devops-monitor:latest
```

Pull the image:

```bash
sudo docker pull ghcr.io/pavankumar-20/devops-monitor:latest
```

Package visibility and registry permissions determine whether authentication is required.

## Stop the Services

```bash
sudo docker compose down
```

## Skills Demonstrated

- Linux administration and command-line troubleshooting
- Python scripting and automated testing
- Docker image creation and container management
- Docker Compose service orchestration
- Prometheus monitoring and metrics collection
- Grafana dashboard configuration
- Git-based version control
- GitHub Actions CI/CD automation
- Container image publishing with GHCR

## Future Improvements

- Add Kubernetes deployment manifests.
- Implement monitoring alerts and notification rules.
- Add application health checks.
- Add code quality and security scanning.
- Deploy the platform to a cloud environment.

## Author

**Pavan Kumar**

GitHub: https://github.com/Pavankumar-20
