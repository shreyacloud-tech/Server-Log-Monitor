# System Health Monitor

## 📌 Project Overview

System Health Monitor is a Python-based command-line monitoring application that checks basic system information and system health.

The application collects CPU, memory, and disk usage information and displays the current health status of the system.

The project is also containerized using Docker and includes a GitHub Actions CI workflow for automated validation.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Monitor basic system resources
- Display operating system information
- Monitor CPU usage
- Monitor memory usage
- Monitor disk usage
- Classify system health status
- Containerize the application using Docker
- Automate validation using GitHub Actions
- Practice Git and GitHub workflows

---

## 🛠️ Technologies Used

- Python 3
- psutil
- Docker
- Git
- GitHub
- GitHub Actions
- Linux
- PowerShell / Windows Terminal

---

## ✨ Features

### 1. System Information

Displays basic information about the operating system, including:

- Operating system name
- Operating system version
- Processor information

### 2. System Health Check

The application checks:

- CPU usage
- Memory usage
- Disk usage

The resource usage is classified into health levels such as:

- NORMAL
- WARNING
- CRITICAL

### 3. Command-Line Interface

The application provides a simple menu-driven interface:

```text
===== SYSTEM HEALTH MONITOR =====

1. System Information
2. Check System Health
3. Exit

4. Docker Support

The application can be packaged and executed inside a Docker container.

5. GitHub Actions CI

GitHub Actions automatically validates the project whenever changes are pushed to the repository.

The CI workflow performs automated checks and builds the Docker image.

📁 Project Structure
System-Health-Monitor
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── .gitignore
├── Dockerfile
├── main.py
└── README.md
🐍 Python Implementation

The application uses the psutil Python library to retrieve system resource information.

The project demonstrates:

Python functions
Conditional statements
User input
System information retrieval
Resource monitoring
Exception handling
Menu-driven applications
🐳 Docker

The application is containerized using Docker.

Build the Docker image
docker build -t system-health-monitor .
Run the Docker container
docker run --rm system-health-monitor

Docker provides an isolated environment in which the Python monitoring application can run.

🔄 GitHub Actions CI

This project includes a GitHub Actions workflow located at:

.github/workflows/ci.yml

The workflow is designed to automatically validate the project when code is pushed to the main branch.

The CI process includes:

Checking out the repository
Setting up Python
Installing required dependencies
Validating the Python application
Building the Docker image

A successful workflow run confirms that the project passes the automated CI checks.

📊 System Monitoring Concepts

This project demonstrates basic monitoring concepts such as:

CPU Monitoring

Measures the percentage of CPU currently being utilized.

Memory Monitoring

Measures the percentage of system memory being used.

Disk Monitoring

Measures the percentage of disk space being utilized.

Health Classification

The collected resource values can be used to identify whether the system is operating normally or experiencing high resource usage.

🧪 Testing

The application was tested locally using Python and Docker.

Python execution:

python main.py

Docker execution:

docker build -t system-health-monitor .
docker run --rm system-health-monitor

The application successfully displays system information and performs system health checks.

📚 What I Learned

Through this project, I learned how to:

Build a Python-based system monitoring application
Use the psutil library
Retrieve CPU, memory, disk, and OS information
Create a menu-driven command-line application
Work with Dockerfiles
Build and run Docker containers
Use Git for version control
Push projects to GitHub
Create GitHub Actions workflows
Implement Continuous Integration
Understand basic system monitoring concepts
🚀 Future Improvements

Possible improvements for this project include:

Add continuous real-time monitoring
Add configurable CPU thresholds
Add configurable memory thresholds
Add configurable disk thresholds
Save monitoring results to a log file
Generate system health reports
Add email alerts
Add notification support
Monitor network usage
Monitor network speed
Add CPU temperature monitoring
Monitor running processes
Create a graphical user interface
Integrate Prometheus
Create Grafana dashboards
Deploy the monitoring application to a cloud environment
Run the monitoring service using Kubernetes
☁️ Cloud & DevOps Relevance

This project demonstrates several skills relevant to Cloud and DevOps engineering:

Linux system monitoring
Python automation
Docker containerization
Git version control
GitHub repository management
Continuous Integration
GitHub Actions
Basic infrastructure monitoring concepts

The project can be further extended using monitoring technologies such as Prometheus and Grafana.

👩‍💻 Author

Salla Shreya

📌 Project Status

Completed

The current version provides basic system information and system health monitoring with Docker containerization and GitHub Actions CI.

Skills Demonstrated
Python
Linux
System Monitoring
psutil
Docker
Git
GitHub
GitHub Actions
Continuous Integration
DevOps Fundamentals
Cloud & Infrastructure Monitoring