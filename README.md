**** "A custom implementation of the Unix command line tool wc, written in Python"****
 
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

**Counting Characters (-m option):**
Description: Counts the number of characters in the specified text file. If the current locale does not support multibyte characters, this will match the -c option.
Usage:
bash
ccwc -m text.txt
Output:  339120 test.txt

**Default Options (Equivalent to -c, -l, -w):**
Description: When no options are provided, the command is equivalent to using -c, -l, and -w together.
Usage:
bash
ccwc text.txt
Output:  7137   58159  341836 test.txt

**Reading from Standard Input:**
Description: Supports reading from standard input if no filename is specified. This allows using the command in a pipeline.
Usage:
bash
cat text.txt | ccwc -l
Output:  7137

# How it Works:
**Command Line Arguments:**
The command-line arguments are processed to determine which counting options to apply.

**File Handling:**
The program reads the specified text file or standard input if no filename is provided.

**Counting Logic:**
Depending on the specified options (-c, -l, -w, -m), the program counts the corresponding metrics (bytes, lines, words, characters).

**Output:**
The program outputs the count information in the specified format.

**Locale Consideration:**
For the -m option, the behavior might depend on the locale settings, and the output is adjusted accordingly.

**Error Handling:**
The program may include error-handling logic to deal with cases such as invalid file paths or incorrect command-line options.

**Code Structure:**
The code is organized into functions or methods to handle different aspects of the counting process, making it modular and easy to maintain.
