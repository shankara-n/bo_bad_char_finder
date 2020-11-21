import sys
import os

print("USAGE: python3 badchars.py <inputFileName> [foundBadChars]")
print("Example: python3 badchars.py xyz 01040d")

# read param - filename
file_name = sys.argv[1]

# read param - bad chars
if len(sys.argv) == 3:
    bad_chars_str = sys.argv[2]
    bad_chars = [bad_chars_str[i:i+2].upper() for i in range(0, len(bad_chars_str), 2)]
else:
    bad_chars = []

# initialise an array with all hex values  like ['01','02' ... 'FF' ]
all_hex = [hex(i)[2:].zfill(2).upper() for i in range(1,256)]

# based on know bad chars, create an expected array
expected_hex = [item for item in all_hex if item not in bad_chars]

# convert input file to one value per line format
# os.system(f'cat {file_name} |  tr " " "\n" > {file_name}.line')
#f = open(f"{file_name}.line", "r")

f = open(file_name, "r")
chars = f.read().replace(" ","\n").split("\n")

for i in range(0,len(expected_hex)):
    if expected_hex[i] != chars[i]:
        print(f"Expected char {expected_hex[i]} but found {chars[i]}")
        sys.exit(0)

print("All Good")
