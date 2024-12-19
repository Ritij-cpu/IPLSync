import json

def format_json(json_string):
  """Formats a JSON string for better readability.

  Args:
    json_string: The JSON string to format.

  Returns:
    The formatted JSON string.
  """

  try:
    parsed_json = json.loads(json_string)
    formatted_json = json.dumps(parsed_json, indent=4)
    return formatted_json
  except json.JSONDecodeError:
    return "Invalid JSON format"

if __name__ == "__main__":
  json_input = input("Enter your JSON data: ")
  formatted_output = format_json(json_input)
  print(formatted_output)