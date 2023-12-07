import argparse

def count_bytes(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    total_count = sum(char_count.values())
    return total_count

def count_lines(file_path):
    try:
        with open(file_path, 'rb') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
        return word_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

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

def main():
    parser = argparse.ArgumentParser(description="Count the number of bytes, lines, and words in a file.")
    parser.add_argument("filename", nargs="?", help="File to count from.")
    parser.add_argument("-c", "--bytes", action="store_true", help="Count bytes instead of lines and words.")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines instead of bytes and words.")
    parser.add_argument("-w", "--words", action="store_true", help="Count words instead of bytes and lines.")
    args = parser.parse_args()

    if args.filename:
        count_type = 'all' if not args.bytes and not args.lines and not args.words else \
                     'bytes' if args.bytes else 'lines' if args.lines else 'words'
        ccwc(args.filename, count_type)
    else:
        print("Error: Please provide a filename.")

if __name__ == "__main__":
    main()
