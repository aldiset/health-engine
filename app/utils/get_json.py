import json

def get_json_from_string(input_string, start: str = "[", end: str = "]"):
    try:
        # Remove unnecessary whitespace and newline characters
        cleaned_string = input_string.strip()

        # Extract the JSON data
        json_start = cleaned_string.find(start)
        json_end = cleaned_string.rfind(end) + 1
        json_data = cleaned_string[json_start:json_end]
        # Load the JSON data
        data = json.loads(json_data)

        return data
    except Exception as e:
        print("Error:", e)
        return None
