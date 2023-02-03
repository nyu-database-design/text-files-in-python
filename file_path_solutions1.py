
# how do you make file paths that work on both Windows and Mac/Linux/Unix?
# the os.path.join() function is one answer for Python 3 versions less than 3.4
# os.path.join() takes a list of strings and joins them together using the correct path separator for the operating system you are using
# note that there is another newer solution to this problem - see the file_path_solutions2.py file

import os


def main():

  # use os.path.join for file paths that are both Windows and Mac/Linx/Unix compatible
  filepath = os.path.join('data', 'jabberwocky.txt') # a relative path
  print(filepath) # on Windows: data\jabberwocky.txt; on Mac/Linux/Unix: data/jabberwocky.txt

  # use os.path.join for file paths that are both Windows and Mac/Linx/Unix compatible
  filepath = os.path.join(os.path.curdir, 'data', 'jabberwocky.txt') # an absolute path
  print(filepath) # on Windows: .\data\jabberwocky.txt; on Mac/Linux/Unix: ./data/jabberwocky.txt

  # a cross-platform file path for a file in the same directory as this file
  filepath = os.path.join(os.path.dirname(__file__), 'data', 'jabberwocky.txt')
  print(filepath) # this may or may not show the same output as the previous example, depending on whether this file is imported into another file or is being run directly

  # a cross-platform file path for a file in the parent directory
  filepath = os.path.join(os.path.pardir, 'text-files-in-python', 'data', 'jabberwocky.txt')
  print(filepath) # on Windows: ..\text-files-in-python\data\jabberwocky.txt; on Mac/Linux/Unix: ../text-files-in-python/data/jabberwocky.txt

  # a cross-platform file path for a file in the home directory
  filepath = os.path.join(os.path.expanduser('~'), 'Desktop', 'foo.txt')
  print(filepath) # on Windows: C:\Users\username\foo.txt; on Mac/Linux/Unix: ~/Desktop/foo.txt


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
