variable "resource_group_name" {
  type        = string
  description = "Name resource group"
  default     = "promtior-rg"
}

variable "location" {
  type        = string
  description = "Azure region"
  default     = "brazilsouth"
}

variable "frontend_image_name" {
  type        = string
  description = "Path image docker for use in backend"
  default = "docker.io/shuhariko/chat-promtior-shuhariko-com"
}

variable "frontend_image_tag" {
  type        = string
  description = "Frontend image tag"
  default     = "c21e76f4322fee7392258e6f00597e9ddcea68c7"
}

variable "backend_image_name" {
  type        = string
  description = "Path image docker for use in backend"
  default = "docker.io/shuhariko/rag-promtior-shuhariko-com"
}

variable "backend_image_tag" {
  type        = string
  description = "Backend image tag"
  default     = "c21e76f4322fee7392258e6f00597e9ddcea68c7"
}