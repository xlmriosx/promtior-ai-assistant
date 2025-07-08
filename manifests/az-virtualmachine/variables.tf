variable "resource_group_name" {
  default = "promtior-rg"
}

variable "location" {
  default = "chilecentral"
}

variable "admin_username" {
  default = "azureuser"
}

variable "vm_size" {
  default = "Standard_B1s"
}

variable "ssh_public_key" {
  description = "SSH public key for the VM"
}