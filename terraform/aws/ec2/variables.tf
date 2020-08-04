variable "instance_type" {
  description = "The name of the instance type"
  default     = "t2.micro"
}
variable "tag_name" {
  description = "The name of the instance tag"
  default     = "pk-gcp-tf-ec2-instance"
}
