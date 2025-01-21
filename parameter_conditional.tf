data "aws_ssm_parameter" "existing" {
  name = "/example/app/config"
}

resource "aws_ssm_parameter" "new_parameter" {
  count = length(data.aws_ssm_parameter.existing.id) == 0 ? 1 : 0

  name  = "/example/app/config"
  value = "novo-valor"
  type  = "String"
}
