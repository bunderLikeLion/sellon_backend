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
