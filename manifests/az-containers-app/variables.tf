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
  default = "docker.io/xlmriosx/chat-promtior-shuhariko-com"
}

variable "frontend_image_tag" {
  type        = string
  description = "Frontend image tag"
  default     = "last commit"
}

variable "backend_image_name" {
  type        = string
  description = "Path image docker for use in backend"
  default = "docker.io/xlmriosx/rag-promtior-shuhariko-com"
}

variable "backend_image_tag" {
  type        = string
  description = "Backend image tag"
  default     = "last commit"
}