locals {
  dynamodb_tables = jsondecode(file("${path.module}/dynamodb_config.json"))
}
