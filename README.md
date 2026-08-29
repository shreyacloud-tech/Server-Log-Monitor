# 🖥️ Server Log Monitor

A Python-based **Server Log Monitoring System** that reads and analyzes server log files from the command line.

This project demonstrates practical Python programming, file handling, log analysis, Git/GitHub, Docker containerization, and GitHub Actions CI.

---

## 📌 Project Overview

Server logs contain important information about the activity and health of a server.

The **Server Log Monitor** reads a server log file and allows users to analyze log entries through a simple command-line interface.

The project is designed to demonstrate how Python can be used to automate basic server-log monitoring tasks.

---

## 🎯 Objectives

The main objectives of this project are:

- Read server log files using Python
- Process and analyze log entries
- Identify different types of log messages
- Search and inspect log information
- Display useful monitoring information
- Practice Python file handling
- Use Git and GitHub for version control
- Containerize the application using Docker
- Automate project checks using GitHub Actions

---

## ✨ Features

### 1. 📄 Server Log File Processing

The application reads information from a server log file and processes the available log entries.

### 2. 🔍 Log Analysis

The application analyzes log information to help understand server activity and identify important log messages.

### 3. 🖥️ Command-Line Interface

The project provides a simple command-line interface that allows users to interact with the monitoring application.

### 4. 📊 Log Monitoring

The application can be used to inspect server log information and identify relevant events from the log file.

### 5. 🐳 Docker Support

The application is containerized using Docker so that it can run in an isolated and reproducible environment.

### 6. ⚙️ GitHub Actions CI

GitHub Actions is configured to automatically run the project's CI workflow whenever changes are pushed to GitHub.

---

## 🛠️ Technologies Used

- **Python 3**
- **Docker**
- **Git**
- **GitHub**
- **GitHub Actions**
- **PowerShell / Command Line**

---

## 📂 Project Structure

```text
Server-Log-Monitor/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── Dockerfile
├── README.md
├── main.py
└── server.log

🐍 Python Implementation

The application is developed using Python.

The project demonstrates concepts such as:

Variables
Functions
Conditional statements
Loops
File handling
String processing
User input
Command-line interaction
Exception handling
📄 Server Log File

The project uses a server.log file as the source of log information.

The log file contains server activity that can be processed by the Python application.

Example log entries:

INFO Server started successfully
INFO User request received
WARNING High memory usage detected
ERROR Database connection failed
INFO Server running normally
🚀 How to Run the Project Locally
Step 1: Clone the Repository
git clone https://github.com/shreyaCloud-tech/Server-Log-Monitor.git
Step 2: Navigate to the Project
cd Server-Log-Monitor
Step 3: Run the Python Application
python main.py
🐳 Running with Docker

Docker is used to package the application and its required files into a container.

Build the Docker Image
docker build -t server-log-monitor .
Run the Docker Container
docker run --rm server-log-monitor

The Docker image contains:

Python runtime
Application code
Server log file
Required project configuration
🔄 Git Workflow

Git is used to track changes to the project.

Basic workflow:

git status
git add .
git commit -m "Update Server Log Monitor"
git push

The project is maintained using a GitHub repository.

⚙️ GitHub Actions

The project includes a GitHub Actions workflow:

.github/
└── workflows/
    └── ci.yml

The CI workflow automatically runs when changes are pushed to the repository.

This helps ensure that the project can be checked automatically instead of relying only on manual testing.

CI Pipeline

The workflow performs automated project checks using GitHub Actions.

Developer
    ↓
Git Commit
    ↓
Git Push
    ↓
GitHub Repository
    ↓
GitHub Actions
    ↓
Python CI
    ↓
Successful Workflow
🐳 Docker Workflow

The complete Docker workflow is:

Python Application
       ↓
   Dockerfile
       ↓
 docker build
       ↓
 Docker Image
       ↓
 docker run
       ↓
Running Container
🧪 Testing

The application was tested locally using Python and Docker.

Python
python main.py
Docker
docker build -t server-log-monitor .
docker run --rm server-log-monitor

The Docker image builds successfully and the container can be started successfully.

📚 What I Learned

Through this project, I practiced:

Python programming
File handling
Reading and processing log files
Command-line applications
Basic server log monitoring concepts
Git version control
GitHub repositories
Git branching
Git commits and pushes
Dockerfile creation
Docker image building
Docker containers
GitHub Actions
Continuous Integration (CI)
Project documentation using Markdown
☁️ Cloud & DevOps Relevance

This project is related to Cloud and DevOps because server-log monitoring is an important part of understanding application and infrastructure behavior.

The project also demonstrates several DevOps practices:

Version Control: Git and GitHub
Containerization: Docker
Continuous Integration: GitHub Actions
Automation: CI workflow
Documentation: Markdown

These concepts form part of a practical Cloud & DevOps workflow.

🔮 Future Improvements

Possible improvements for the project include:

Add real-time log monitoring
Monitor logs continuously
Add configurable log-level filtering
Add error and warning counters
Generate monitoring reports
Save monitoring results to a separate file
Add timestamp-based filtering
Add network monitoring
Add email or notification alerts
Add a web-based dashboard
Integrate the project with cloud monitoring services
Deploy the application to a cloud environment
Improve the Docker deployment workflow
📌 Project Status

Completed

The project currently includes:

✅ Python application
✅ Server log file
✅ README documentation
✅ .gitignore
✅ Dockerfile
✅ Docker image build
✅ Docker container execution
✅ Git repository
✅ GitHub repository
✅ GitHub Actions CI
👩‍💻 Author

Salla Shreya

⭐ Conclusion

The Server Log Monitor project demonstrates how Python can be combined with Docker, GitHub, and GitHub Actions to create a simple but practical monitoring application.

It provides hands-on experience with Python development, containerization, version control, and Continuous Integration, making it a useful project for building a Cloud & DevOps portfolio.