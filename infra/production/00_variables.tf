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


# logs

variable "log_retention_in_days" {
  default = 30
}
