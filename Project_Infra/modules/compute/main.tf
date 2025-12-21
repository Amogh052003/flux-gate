resource "azurerm_public_ip" "jenkins" {
  name                = "PIP-Jenkins-1"
  resource_group_name = var.resource_group_name
  location            = var.location
  allocation_method   = "Static"
  sku                 = "Standard"
  ip_version          = "IPv4"
}

resource "azurerm_public_ip" "sonarqube" {
  name                = "PIP-SonarQube-1"
  resource_group_name = var.resource_group_name
  location            = var.location
  allocation_method   = "Static"
  sku                 = "Standard"
  ip_version          = "IPv4"
}

resource "azurerm_network_interface" "jenkins" {
  name                = var.network_interface_jenkins
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.jenkins.id
  }
}

resource "azurerm_network_interface" "sonarqube" {
  name                = var.network_interface_sonarqube
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.sonarqube.id
  }
}


resource "azurerm_linux_virtual_machine" "jenkins" {
  name                = var.vm_jenkins
  resource_group_name = var.resource_group_name
  location            = var.location
  size                = "Standard_D2ds_v4"
  admin_username      = var.admin_username

  network_interface_ids = [
    azurerm_network_interface.jenkins.id
  ]

  admin_ssh_key {
    username   = var.admin_username
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}

resource "azurerm_linux_virtual_machine" "sonarqube" {
  name                = var.vm_sonarqube
  resource_group_name = var.resource_group_name
  location            = var.location
  size                = "Standard_D2ds_v4"
  admin_username      = var.admin_username

  network_interface_ids = [
    azurerm_network_interface.sonarqube.id
  ]

  admin_ssh_key {
    username   = var.admin_username
    public_key = file("~/.ssh/id_rsa.pub")
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}



