
# how do you make file paths that work on both Windows and Mac/Linux/Unix?
# the Path module is one answer for Python 3 versions greater than 3.4
# note that there is another older solution to this problem for earlier versions of Python - see the file_path_solutions1.py file

from pathlib import Path
import os

def main():

  # use Path for file paths that are both Windows and Mac/Linx/Unix compatible
  filepath = Path('data/jabberwocky.txt')
  print(filepath) # on Windows: data\jabberwocky.txt; on Mac/Linux/Unix: data/jabberwocky.txt

  # use the resolve() method of any Path object to get the absolute path
  filepath = Path('data/jabberwocky.txt').resolve()
  print(filepath)

  # get the current directory's full absolute path
  filepath = Path(os.path.curdir).resolve()
  print(filepath)

  # get the root directory path
  filepath = Path('/')
  print(filepath) # on Windows: \; on Mac/Linux/Unix: /

  # note that the Path object is not a string... you can easily convert it to one with the str() function
  print(type(filepath))
  print(type(str(filepath)))

# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
