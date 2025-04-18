param (
    [string]$cloudProvider = "aws"
)

Write-Host "Deploying to $cloudProvider..."
switch ($cloudProvider) {
    "aws" {
        terraform -chdir=terraform/aws init
        terraform -chdir=terraform/aws apply -auto-approve
    }
    "gcp" {
        terraform -chdir=terraform/gcp init
        terraform -chdir=terraform/gcp apply -auto-approve
    }
    "azure" {
        terraform -chdir=terraform/azure init
        terraform -chdir=terraform/azure apply -auto-approve
    }
    default {
        Write-Error "Invalid cloud provider. Use 'aws', 'gcp', or 'azure'."
    }
}
