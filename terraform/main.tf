terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "django_app" {
  name         = "django-app:latest"
  keep_locally = true
}

resource "docker_container" "django_app" {
  name  = "django_app_container"
  image = docker_image.django_app.name

  ports {
    internal = 8000
    external = 8000
  }
}
