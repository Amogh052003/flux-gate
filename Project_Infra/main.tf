terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

module "rg" {
  source = "./modules/resource_group"
  name   = var.resource_group_name
  location = var.location
}

module "network" {
  source = "./modules/network"
  vnet_name = var.vnet_name
  address_space = var.vnet_address_space
  subnets = var.subnets
  resource_group_name = module.rg.name
  location = module.rg.location
}

module "compute" {
  source = "./modules/compute"
  admin_username = var.admin_username
  resource_group_name = module.rg.name
  location = module.rg.location
  subnet_id = module.network.subnet_ids[0]
  vm_jenkins = var.vm_jenkins
  vm_sonarqube = var.vm_sonarqube
  vm_nexus = var.vm_nexus
  network_interface_jenkins = var.network_interface_jenkins
  network_interface_sonarqube = var.network_interface_sonarqube
  network_interface_nexus = var.network_interface_nexus
}
