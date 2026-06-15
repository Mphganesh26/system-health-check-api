terraform {
  required_version = ">= 1.0"
}

provider "local" {}

resource "local_file" "deployment_info" {
  filename = "deployment.txt"
  content  = "System Health Check API Terraform Deployment"
}