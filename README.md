# FlaskSecureCloud 🚀

A secure and scalable Flask web application with JWT-based authentication, Docker containerization, and deployment to Google Cloud Run using Terraform.

---

## 📌 Table of Contents

- [Overview]
- [Features]
- [Tech Stack]
- [Project Structure]
- [Getting Started]
- [Terraform Deployment]
- [Cloud Run Deployment with Docker]

## 🌐 Overview

**FlaskSecureCloud** is a web application built using Python and Flask that enables users to securely sign up, log in, and access a protected dashboard. It uses **JWT (JSON Web Tokens)** for authentication and **SQLite** for data storage in development. The app is containerized with **Docker** and deployed to **Google Cloud Run**, with infrastructure managed via **Terraform**.

---

## ✅ Features

- 🔐 Secure Signup/Login with hashed passwords and JWT cookies
- 👤 Protected user dashboard
- 🧪 `/health` endpoint for health checks
- 🐳 Docker containerization for portability
- ☁️ Google Cloud Run deployment for serverless execution
- ⚙️ Infrastructure as Code using Terraform

---

## 🛠️ Tech Stack

- **Frontend**: HTML, Jinja2 Templates
- **Backend**: Python, Flask
- **Auth**: JWT (JSON Web Tokens)
- **Database**: SQLite
- **Containerization**: Docker
- **Cloud Platform**: Google Cloud Platform (Cloud Run)
- **IaC**: Terraform
- **Web Server**: Gunicorn


## 📁 Project Structure

FlaskSecureCloud/
├── app/
│ ├── main.py
│ ├── requirements.txt
│ └── templates/
│ ├── login.html
│ ├── signup.html
│ └── dashboard.html
├── Dockerfile
├── .gitignore
└── terraform/
├── main.tf
├── variables.tf
├── terraform.tfvars
└── .terraform.lock.hcl


## ⚙️ Getting Started (Local Setup)

1. **Clone the Repository**  
   git clone https://github.com/Workarjun/FlaskSecureCloud.git
   cd FlaskSecureCloud

Set up a virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies
pip install -r app/requirements.txt

Run the app
python app/main.py

☁️ Terraform Deployment
Update terraform.tfvars
Replace values with your actual GCP project and region:

project_id = "your-gcp-project-id"
region     = "us-central1"


Initialize Terraform and apply

cd terraform/
terraform init
terraform apply
Output:
After successful deployment, Terraform will show the Cloud Run service URL.

🐳 Cloud Run Deployment with Docker

Build Docker Image

docker build -t gcr.io/healthy-highway-426311-i0/flask-app .

Push to Artifact Registry (or Container Registry)

docker push gcr.io/healthy-highway-426311-i0/flask-app

Deploy via Terraform or gcloud CLI