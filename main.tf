provider "aws" {
  region = var.region
}

# Use the local variable defined in data.tf
# Assuming `dynamodb_tables` is defined in data.tf as:
# locals {
#   dynamodb_tables = jsondecode(file("${path.module}/dynamodb_config.json"))
# }

# Resource for PAY_PER_REQUEST tables
resource "aws_dynamodb_table" "dynamodb_tables" {
  for_each = { for table in local.dynamodb_tables : table.TableName => table }

  name         = each.value.TableName
  billing_mode = "PAY_PER_REQUEST"

  # Key schema
  hash_key  = lookup({ for ks in each.value.KeySchema : ks.KeyType => ks.AttributeName }, "HASH", null)
  range_key = lookup({ for ks in each.value.KeySchema : ks.KeyType => ks.AttributeName }, "RANGE", null)

  # Attribute definitions
  dynamic "attribute" {
    for_each = each.value.AttributeDefinitions
    content {
      name = attribute.value.AttributeName
      type = attribute.value.AttributeType
    }
  }

  # Stream specification
  # stream_enabled   = each.value.StreamSpecification.StreamEnabled
  # stream_view_type = lookup(each.value.StreamSpecification, "StreamViewType", null)

  # Global Secondary Indexes
  dynamic "global_secondary_index" {
    for_each = lookup(each.value, "GlobalSecondaryIndexes", [])
    content {
      name               = global_secondary_index.value.IndexName
      hash_key           = lookup({ for ks in global_secondary_index.value.KeySchema : ks.KeyType => ks.AttributeName }, "HASH", null)
      range_key          = lookup({ for ks in global_secondary_index.value.KeySchema : ks.KeyType => ks.AttributeName }, "RANGE", null)
      projection_type    = global_secondary_index.value.Projection.ProjectionType
      non_key_attributes = lookup(global_secondary_index.value.Projection, "NonKeyAttributes", null)

      # Do not include read_capacity and write_capacity since billing_mode is PAY_PER_REQUEST
    }
  }

  # Local Secondary Indexes
  dynamic "local_secondary_index" {
    for_each = lookup(each.value, "LocalSecondaryIndexes", [])
    content {
      name               = local_secondary_index.value.IndexName
      range_key          = lookup({ for ks in local_secondary_index.value.KeySchema : ks.KeyType => ks.AttributeName }, "RANGE", null)
      projection_type    = local_secondary_index.value.Projection.ProjectionType
      non_key_attributes = lookup(local_secondary_index.value.Projection, "NonKeyAttributes", null)
    }
  }
}
