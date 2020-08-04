resource "aws_instance" "myInstance" {
  ami           = "ami-0a13d44dccf1f5cf6"
  instance_type = var.instance_type
  tags = {
     Name = var.tag_name
  }
  user_data     = <<-EOF
                  #!/bin/bash
                  sudo su
                  yum -y install httpd
                  echo "<p> My Instance! </p>" >> /var/www/html/index.html
                  sudo systemctl enable httpd
                  sudo systemctl start httpd
                  EOF
}
