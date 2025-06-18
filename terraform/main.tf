provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_service" "flask_app" {
  name     = "flask-app"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/flask-app:latest"
        env {
          name  = "PORT"
          value = "8080"
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

output "service_url" {
  value = google_cloud_run_service.flask_app.status[0].url
}
