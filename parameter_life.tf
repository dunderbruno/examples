resource "aws_ssm_parameter" "example" {
  name        = "/example/app/config"
  value       = "valor-novo"
  type        = "String"
  overwrite   = false

  lifecycle {
    ignore_changes = [value]
  }
}
