# Chapter 11: Files

This chapter covers how to persist data by reading from and writing to files on a disk, rather than relying on volatile memory (variables).

## 1. Opening Files
To interact with a file, you must first create a file handle using `open()`.

* **Syntax:** handle = open(filename, mode)
* **Modes:**
    * 'r' (Read): Default. Reading only. Errors if the file is missing.
    * 'w' (Write): Writing. **Overwrites** existing files; creates a new one if it doesn't exist.
    * 'a' (Append): Writes data to the end of the file without deleting existing content.

## 2. Reading Methods
Once a file is open in 'r' mode:

* .read(): Reads the *entire* file into a single string.
* .readline(): Reads a single line (up to and including the \n).
* .readlines(): Returns a list where each element is a line string.

**The "For Loop" approach (Best Practice):**
Python treats the file handle as an iterator. This is memory efficient.

    infile = open("data.txt", "r")
    for line in infile:
        print(line) # Note: line usually contains a trailing newline

## 3. Writing Methods
* .write(string): Writes a string to the file.
* **Important:** Unlike print(), .write() does **not** add a newline automatically. You must explicitly add \n.

## 4. Closing Files
* .close(): Frees up system resources. If you forget this, data might not be saved or the file might remain "locked."

## 5. The `with` Statement (Context Managers)
This is the modern, Pythonic way to open files. It automatically closes the file even if the program crashes inside the block.

    with open("mydata.txt", "r") as f:
        content = f.read()
    # File is now closed automatically

## 6. Working with Binary Files
* Text files contain readable characters.
* Binary files (images, audio) must be opened with 'b' mode (e.g., 'rb' or 'wb').