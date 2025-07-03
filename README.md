**INTRODUCTION**

This project is a minimal and secure web application built using Flask that provides JWT-based user authentication (signup, login, logout) with a protected dashboard route. It is containerized using Docker, deployed to Google Cloud Run, and the infrastructure is managed using Terraform. The goal is to demonstrate a clean and scalable deployment pipeline for a simple web application on the cloud.

📌**Project Overview**

The application allows users to sign up and log in securely. Authenticated users receive a JWT (JSON Web Token), which is stored in a browser cookie and is used to protect routes like /dashboard. The project uses a simple HTML interface (no JS), a lightweight SQLite3 database for storage, and a secure Flask backend that handles authentication and routing.

To keep the setup modern and cloud-native, the application is containerized using Docker, deployed to Google Cloud Run, and provisioned using Terraform. Additionally, CI/CD can be added using Google Cloud Build to automatically build, push, and deploy the application on every commit.


⚙️ **Technologies Used**

Flask – Python web framework

JWT – Secure token-based authentication

SQLite3 – Lightweight local database

Docker – Containerization of the application

Google Cloud Run – Serverless deployment

Terraform – Infrastructure as Code (IaC) for provisioning

Cloud Build (Optional) – CI/CD pipeline for auto deployment

🚀 **Running the Application**

🔧 Local Setup (for testing)

You can run the app locally using:

cd app
python main.py

The app will start on http://localhost:5000. You can access the login/signup pages from here.

🐳 **Docker Deployment**

To containerize and run the app locally:

docker build -t flask-app .
docker run -p 8080:8080 flask-app

Visit http://localhost:8080

☁️ **Deploying to Google Cloud Run using Terraform**

Authenticate with Google Cloud:
gcloud auth login
gcloud config set project your-project-id

Build and push the Docker image:
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/flask-app

Apply Terraform to deploy Cloud Run:
cd terraform
terraform init
terraform apply
After deployment, Terraform will output the live Cloud Run URL of your application.


🔐 **How JWT Authentication Works**

The app uses JWT tokens for secure session management:

Login: When a user logs in, a token is generated with their username and expiration time.

Cookie: The token is stored in a browser cookie (token) for use on future requests.

Protected Routes: Routes like /dashboard are protected with a @token_required decorator that checks the validity of the token.

Logout: Logging out simply clears the cookie, effectively removing the token.
