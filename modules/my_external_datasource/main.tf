data external person {
  program = ["python3", "${path.module}/scripts/person.py"]

  query {
    some_query_attribute = "${var.some_query_attribute}"
  }
}
