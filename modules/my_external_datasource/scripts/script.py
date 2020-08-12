#!/usr/bin/env python
import sys
import json

import sys

def obtain_query_data():
  json_input = ''

  for line in sys.stdin:
      json_input += line

  return json.loads(json_input.rstrip())

def fetch_data(query_data):
  ## fetch data to serve as data source
  # query_data['some_query_attribute']
  return {}

def return_new_state(resource):
  print(json.dumps(resource))
  sys.exit(0)

def main():
  query_data = obtain_query_data()

  data = fetch_data(query_data)

  return_new_state(resource=data)

main()
