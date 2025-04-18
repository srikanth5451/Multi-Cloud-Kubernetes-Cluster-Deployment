provider "azurerm" {
  features {}
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = "multi-cloud-aks"
  location            = "East US"
  resource_group_name = "your-resource-group"
  dns_prefix          = "aks"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_B2s"
  }
}
