#Task 1:


# text_utils.py

def reverse_string(s):
    """Function to reverse a string"""
    return s[::-1]

def capitalize_string(s):
    """Function to capitalize a string"""
    return s.capitalize()

# Main program logic
def main():
    test_string = "hello world"
    
    # Use functions from text_utils directly
    reversed_string = reverse_string(test_string)
    capitalized_string = capitalize_string(test_string)
    
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reversed_string}")
    print(f"Capitalized string: {capitalized_string}")

if __name__ == "__main__":
    main()
