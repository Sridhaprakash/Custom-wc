**** "A custom implementation of the Unix command line tool wc, written in Python"****

**Usage**
bash
python file_counter.py <filename> [-c] [-l] [-w]
<filename>: The path to the file you want to analyze.
-c or --bytes: Count the number of bytes in the file.
-l or --lines: Count the number of lines in the file.
-w or --words: Count the number of words in the file.

**Functions**
count_bytes(input_string)
Counts the number of bytes in a given string.

count_lines(file_path)
Counts the number of lines in a file, handling different line endings.

count_words(file_path)
Counts the number of words in a file.

ccwc(filename, count_type='all')
Combines the functionalities to count bytes, lines, and words based on the specified count_type.
Prints the results for the selected count type.

# Features:
**Counting Bytes (-c option):**
Description: Counts the number of bytes in the specified text file.
Usage:
bash
ccwc -c text.txt
Output:  341836 test.txt

**Counting Lines (-l option):**
Description: Counts the number of lines in the specified text file.
Usage:
bash
ccwc -l text.txt
Output:  7137 test.txt

**Counting Words (-w option):**
Description: Counts the number of words in the specified text file.
Usage:
bash
ccwc -w text.txt
Output:  58159 test.txt

**Default Options (Equivalent to -c, -l, -w):**
Description: When no options are provided, the command is equivalent to using -c, -l, and -w together.
Usage:
bash
ccwc text.txt
Output:  7137   58159  341836 test.txt
ogic to deal with cases such as invalid file paths or incorrect command-line options.



**Code Structure:**
The code is organized into functions or methods to handle different aspects of the counting process, making it modular and easy to maintain.
