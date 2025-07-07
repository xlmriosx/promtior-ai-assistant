resource "azurerm_resource_group" "main" {
    name     = var.resource_group_name
    location = var.location
}

resource "azurerm_virtual_network" "main" {
    name                = "promtior-vnet"
    address_space       = ["10.0.0.0/16"]
    location            = azurerm_resource_group.main.location
    resource_group_name = azurerm_resource_group.main.name
}

resource "azurerm_subnet" "main" {
    name                 = "promtior-subnet"
    resource_group_name  = azurerm_resource_group.main.name
    virtual_network_name = azurerm_virtual_network.main.name
    address_prefixes     = ["10.0.1.0/24"]

    depends_on = [azurerm_virtual_network.main]
}

resource "azurerm_public_ip" "main" {
    name                = "promtior-public-ip"
    location            = azurerm_resource_group.main.location
    resource_group_name = azurerm_resource_group.main.name
    allocation_method   = "Static"
}

resource "azurerm_network_interface" "main" {
    name                = "promtior-nic"
    location            = azurerm_resource_group.main.location
    resource_group_name = azurerm_resource_group.main.name

    ip_configuration {
        name                          = "internal"
        subnet_id                     = azurerm_subnet.main.id
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id          = azurerm_public_ip.main.id
    }
}

resource "azurerm_linux_virtual_machine" "main" {
    name                = "promtior-vm"
    resource_group_name = azurerm_resource_group.main.name
    location            = azurerm_resource_group.main.location
    size                = "Standard_D4s_v3"
    admin_username      = "ollamaadmin"
    network_interface_ids = [
        azurerm_network_interface.main.id,
    ]
    os_disk {
        caching              = "ReadWrite"
        storage_account_type = "Standard_LRS"
        name                 = "osdisk"
    }
    source_image_reference {
        publisher = "Canonical"
        offer     = "0001-com-ubuntu-server-jammy"
        sku       = "22_04-lts-gen2"
        version   = "latest"
    }
    computer_name  = "promtiorvm"
    admin_ssh_key {
        username   = "ollamaadmin"
        public_key = var.ssh_public_key
    }
}

resource "azurerm_network_interface_security_group_association" "main" {
  network_interface_id      = azurerm_network_interface.main.id
  network_security_group_id = azurerm_network_security_group.main.id
}

resource "azurerm_network_security_group" "main" {
  name                = "promtior-nsg"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  security_rule {
        name                       = "AllowSSH"
        priority                   = 1000
        direction                  = "Inbound"
        access                     = "Allow"
        protocol                   = "Tcp"
        source_port_range          = "*"
        destination_port_range     = "22"
        source_address_prefix      = "*"
        destination_address_prefix = "*"
  }

}

output "public_ip_address" {
  description = "The public IP address of the VM"
  value       = azurerm_public_ip.main.ip_address
}