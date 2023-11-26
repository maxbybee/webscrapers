import re

def keep_numbers_only(input_string):
    # Use regular expression to remove non-numeric characters
    numbers_only = re.sub(r'\D', '', input_string)
    return numbers_only

# Example usage:

if __name__ == '__main__':

    input_text = "abc123def456ghi789"
    result = keep_numbers_only(input_text)
    print("Input Text:", input_text)
    print("Numbers Only:", result)
