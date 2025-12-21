output "jenkins_vm_id" {
  description = "ID of the Jenkins virtual machine"
  value       = azurerm_linux_virtual_machine.jenkins.id
}

output "sonarqube_vm_id" {
  description = "ID of the SonarQube virtual machine"
  value       = azurerm_linux_virtual_machine.sonarqube.id
}

output "nexus_vm_id" {
  description = "ID of the Nexus virtual machine"
  value       = azurerm_linux_virtual_machine.nexus.id
}

output "jenkins_public_ip" {
  description = "Public IP address for Jenkins"
  value       = azurerm_public_ip.jenkins.ip_address
}

output "sonarqube_public_ip" {
  description = "Public IP address for SonarQube"
  value       = azurerm_public_ip.sonarqube.ip_address
}

output "nexus_public_ip" {
  description = "Public IP address for Nexus"
  value       = azurerm_public_ip.nexus.ip_address
}

output "jenkins_private_ip" {
  description = "Private IP address for Jenkins"
  value       = azurerm_network_interface.jenkins.ip_configuration[0].private_ip_address
}

output "sonarqube_private_ip" {
  description = "Private IP address for SonarQube"
  value       = azurerm_network_interface.sonarqube.ip_configuration[0].private_ip_address
}

output "nexus_private_ip" {
  description = "Private IP address for Nexus"
  value       = azurerm_network_interface.nexus.ip_configuration[0].private_ip_address
}
