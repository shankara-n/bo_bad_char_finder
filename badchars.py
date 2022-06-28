import sys
import os


class bcolors:
    BOLD = '\033[1m'
    OKBLUE = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def fprint(a,style):
    print(style + a + bcolors.ENDC)

fprint("[*] USAGE: python3 badchars.py <inputFileName> [foundBadChars]",bcolors.BOLD)
fprint("[*] Example: python3 badchars.py xyz 01040d\n",bcolors.BOLD)

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
f = open(file_name, "r")
chars = f.read().replace(" ","\n").split("\n")
print("Here is your input ...")
print(chars)

for i in range(0,len(expected_hex)):
    if expected_hex[i] != chars[i]:
        fprint(f"\n[!] Expected char {expected_hex[i]} after char {expected_hex[i-1]} but found {chars[i]} instead!\n",bcolors.FAIL)
        sys.exit(0)

fprint("[*] All Good!", bcolors.OKBLUE)
