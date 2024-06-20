```markdown
# 0x03. Log Parsing

## Description

This project involves reading log entries from standard input (stdin), parsing the data, and computing statistics in real-time. The goal is to handle data streams efficiently, processing each line of input to extract key information and periodically outputting summary statistics.

## Concepts and Resources

To successfully complete this project, you should familiarize yourself with the following concepts:

- **File I/O in Python**: Learn how to read from `sys.stdin` line by line.
  - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- **Signal Handling in Python**: Understand how to handle keyboard interruptions (CTRL + C).
  - [Python Signal Handling](https://docs.python.org/3/library/signal.html)
- **Data Processing**: Parse strings to extract data points and aggregate data.
- **Regular Expressions**: Use regex to validate and parse input lines.
  - [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- **Dictionaries in Python**: Use dictionaries to count status codes and accumulate file sizes.
  - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- **Exception Handling**: Handle possible exceptions during file reading and data processing.
  - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Requirements

- **Editors**: `vi`, `vim`, `emacs`
- **Interpreter**: Python 3.4.3
- **Style**: Code should use PEP 8 style (version 1.7.x)
- **Files**: All files should end with a new line and be executable

## Task

### 0. Log Parsing

Write a script that reads stdin line by line and computes metrics:

- **Input format**: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- **Output**: 
  - After every 10 lines and/or a keyboard interruption (CTRL + C), print:
    - `File size: <total size>` where `<total size>` is the sum of all file sizes.
    - Number of lines by status code in ascending order:
      - `200: <count>`
      - `301: <count>`
      - `400: <count>`
      - `401: <count>`
      - `403: <count>`
      - `404: <count>`
      - `405: <count>`
      - `500: <count>`

### Example

```shell
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Implementation

Create a script `0-stats.py` that reads stdin, processes log entries, and computes the required statistics. Ensure the script handles interruptions gracefully and outputs the statistics in the specified format.

## Usage

Run the provided generator script and pipe its output to your `0-stats.py` script to test the log parsing functionality:

```shell
./0-generator.py | ./0-stats.py
```