[
  {
    "name": "sellon-webapp",
    "image": "${webapp_image_url}",
    "essential": true,
    "cpu": 10,
    "memory": 512,
    "links": [],
    "portMappings": [
      {
        "containerPort": 8888,
        "hostPort": 0,
        "protocol": "tcp"
      }
    ],
    "environment": [],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/webapp-production",
        "awslogs-region": "${region}",
        "awslogs-stream-prefix": "webapp-production-log-stream"
      }
    }
  }
]
