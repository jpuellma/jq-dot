import sys
import json

# comments
def format_json():
    # Read JSON from standard input
    input_json = sys.stdin.read()
    
    try:
        # Parse the JSON
        parsed_json = json.loads(input_json)
        
        # Format the JSON
        formatted_json = json.dumps(parsed_json, indent=4)
        
        # Output the formatted JSON
        print(formatted_json)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input. {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    format_json()

