resource "aws_cloudwatch_log_group" "webapp-log-group" {
  name              = "/ecs/webapp-production"
  retention_in_days = var.log_retention_in_days
}

resource "aws_cloudwatch_log_stream" "webapp-log-stream" {
  name           = "webapp-production-log-stream"
  log_group_name = aws_cloudwatch_log_group.webapp-log-group.name
}
