variable "admin_username" {
  description = "Administrator username for the virtual machines"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
}

variable "subnet_id" {
  description = "ID of the subnet to attach network interfaces to"
  type        = string
}

variable "vm_jenkins" {
  description = "Name of the Jenkins VM"
  type        = string
}

variable "vm_sonarqube" {
  description = "Name of the SonarQube VM"
  type        = string
}

variable "vm_nexus" {
  description = "Name of the Nexus VM"
  type        = string
}

variable "network_interface_jenkins" {
  description = "Name of the Jenkins network interface"
  type        = string
}

variable "network_interface_sonarqube" {
  description = "Name of the SonarQube network interface"
  type        = string
}

variable "network_interface_nexus" {
  description = "Name of the Nexus network interface"
  type        = string
}


