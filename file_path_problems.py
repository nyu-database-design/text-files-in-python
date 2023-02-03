

# reminder of how escape characters work in Python
my_string1 = 'foo\nbar' # a string with a line break
my_string2 = 'foo\tbar' # a string with a tab
my_string3 = 'foo\\bar' # a string with a single backslash

# raw strings allow you to safely write strings that contain characters that would be considered escape characters in regular strings
my_string4 = r'foo\bar' # the backslash is just a backslash in this raw string

# file paths in Windows require backslashes, which have to be escaped, leading to very confusing-looking text
file_path0 = "C:\\Users\\foobarstein\\Desktop\\foo.txt"

# one way to simplify how Windows-specific file paths are written is to use "raw strings" in Python
file_path1 = r"C:\Users\foobarstein\Desktop\foo.txt"

# Mac/Linux/Unix file paths, on the other hand, use forward slashes, which do not create a problem
file_path2 = '/Users/foobarstein/Desktop/foo.txt'

# so you see... file paths are problematic on Windows
# and are different on Mac/Linux/Unix versus Windows
# ... see the file_path_solutions.py file for better ways to handle file paths
