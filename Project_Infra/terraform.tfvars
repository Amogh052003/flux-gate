vnet_name          = "Main-Vnet"
vnet_address_space = ["10.0.0.0/16"]

subnets = [
  {
    name           = "Subnet-1"
    address_prefix = "10.0.2.0/24"
  }
]

resource_group_name = "fluxgate-rg-01"
admin_username      = "amogh"
location            = "East US"

network_interface_jenkins   = "NIC-Jenkins-1"
network_interface_sonarqube = "NIC-SonarQube-1"
network_interface_nexus     = "NIC-Nexus-1"

vm_jenkins   = "VM-Jenkins-1"
vm_sonarqube = "VM-SonarQube-1"
vm_nexus     = "VM-Nexus-1"
