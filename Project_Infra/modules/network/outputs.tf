output "vnet_id" {
  description = "ID of the virtual network"
  value       = azurerm_virtual_network.main.id
}

output "vnet_name" {
  description = "Name of the virtual network"
  value       = azurerm_virtual_network.main.name
}

output "subnet_ids" {
  description = "IDs of the subnets created"
  value       = azurerm_subnet.main[*].id
}

output "subnet_names" {
  description = "Names of the subnets created"
  value       = azurerm_subnet.main[*].name
}

output "subnet_address_prefixes" {
  description = "Primary address prefix for each subnet"
  value       = [for s in azurerm_subnet.main : s.address_prefixes[0]]
}
