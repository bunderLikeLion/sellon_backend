# network

variable "public_subnet_1_cidr" {
  description = "CIRR BLOCK for Public Subnet 1"
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr" {
  description = "CIRR BLOCK for Public Subnet 1"
  default     = "10.0.2.0/24"
}


variable "private_subnet_1_cidr" {
  description = "CIRR BLOCK for Private Subnet 1"
  default     = "10.0.3.0/24"
}

variable "private_subnet_2_cidr" {
  description = "CIRR BLOCK for Private Subnet 2"
  default     = "10.0.4.0/24"
}

variable "availability_zones" {
  type        = list(string)
  description = "Availability zones"
  default     = ["ap-northeast-2a", "ap-northeast-2b"]
}


# load balancer

variable "health_check_path" {
  description = "Health check path for the default target group"
  default     = "/health-check/"
}


# ecs

variable "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  default     = "production"
}

variable "amis" {
  description = "Which AMI to spawn."
  default = {
    ap-northeast-2 = "ami-0fddf6737a5d12089"
  }
}

variable "instance_type" {
  default = "t2.micro"
}

variable "webapp_image_url" {
  description = "Docker image to run in the ECS cluster"
  default     = "741892569245.dkr.ecr.ap-northeast-2.amazonaws.com:latest"
}

variable "app_count" {
  description = "Number of Docker containers to run"
  default     = 1
}

# logs

variable "log_retention_in_days" {
  default = 30
}


# keypair

variable "ssh_pubkey_file" {
  description = "Path to an SSH public key"
  default     = "~/.ssh/id_rsa.pub"
}
