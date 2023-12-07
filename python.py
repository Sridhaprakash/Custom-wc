# Import the argparse module for parsing command-line arguments
import argparse

# Function to count the number of bytes in a string
def count_bytes(input_string):
    # Dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the input string
    for char in input_string:
        # Update the count for the current character
        char_count[char] = char_count.get(char, 0) + 1
    
    # Sum the counts of all characters
    total_count = sum(char_count.values())
    
    # Return the total count
    return total_count

# Function to count the number of lines in a file
def count_lines(file_path):
    try:
        # Open the file in binary mode ('rb') to handle different line endings
        with open(file_path, 'rb') as file:
            # Use a generator expression to count lines efficiently
            line_count = sum(1 for line in file)
        
        # Return the count of lines
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to count the number of words in a file
def count_words(file_path):
    try:
        # Open the file in text mode ('r')
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()
            
            # Split the content into words and count them
            word_count = len(content.split())
        
        # Return the count of words
        return word_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to count bytes, lines, and words based on count_type
def ccwc(filename, count_type='all'):
    if count_type == 'all':
        bytes_result = count_bytes(filename)
        lines_result = count_lines(filename)
        words_result = count_words(filename)
        print(f"Bytes: {bytes_result}  Lines: {lines_result}  Words: {words_result}  File: {filename}")
    elif count_type == 'bytes':
        bytes_result = count_bytes(filename)
        print(f"Bytes: {bytes_result}  File: {filename}")
    elif count_type == 'lines':
        lines_result = count_lines(filename)
        print(f"Lines: {lines_result}  File: {filename}")
    elif count_type == 'words':
        words_result = count_words(filename)
        print(f"Words: {words_result}  File: {filename}")
    else:
        print(f"Error: Invalid count type '{count_type}'. Supported types are 'all', 'bytes', 'lines', and 'words'.")
        return None

# Main function for handling command-line arguments and executing the counting
def main():
    # Create an ArgumentParser object with a description
    parser = argparse.ArgumentParser(description="Count the number of bytes, lines, and words in a file.")
    
    # Define command-line arguments
    parser.add_argument("filename", nargs="?", help="File to count from.")
    parser.add_argument("-c", "--bytes", action="store_true", help="Count bytes instead of lines and words.")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines instead of bytes and words.")
    parser.add_argument("-w", "--words", action="store_true", help="Count words instead of bytes and lines.")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if a filename is provided
    if args.filename:
        # Determine the count type based on the provided options
        count_type = 'all' if not args.bytes and not args.lines and not args.words else \
                     'bytes' if args.bytes else 'lines' if args.lines else 'words'
        
        # Call the ccwc function with the specified filename and count type
        ccwc(args.filename, count_type)
    else:
        # Display an error message if no filename is provided
        print("Error: Please provide a filename.")

# Check if the script is executed as the main program
if __name__ == "__main__":
    # Call the main function
    main()
