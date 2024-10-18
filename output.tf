output "dynamodb_table_names" {
  description = "Names of the created DynamoDB tables"
  value       = [for table in aws_dynamodb_table.dynamodb_tables : table.name]
}
