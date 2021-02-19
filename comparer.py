import argparse
import os
from colorama import Fore, Back, Style

# Test for specific lengths or range of langths 
# test for entropy - does it change a lot? 

inhndle = open('input.txt', 'r').readlines()

# Compare characters in each line at specific position
# i.e. in abc \n abc a is compared to a etc. 
def compareCharacterAtPosition(startline = 0):
    # Print first line and separator
    print(inhndle[startline], end='')
    print(Fore.WHITE + "=" * 60)
    for line in set(inhndle) - {inhndle[startline]}:
        for i,v in enumerate(line):
            # For cases when startline is shorter than the other lines
            try: 
                # Skip newlines - it's printed after try block
                if v == '\n':
                    continue
                # If matched character and position, print it green
                if v == inhndle[startline][i]:
                    print(Fore.GREEN + v, end="")
                # Otherwise, white
                else:
                    print(Fore.WHITE + v, end="")
            except IndexError:
                print(Fore.WHITE + v, end="")
        print()
    
    print(Fore.WHITE + "=" * 60)
#

# Compare whether any of substrings of specified length
# appear in other lines
def compareSubstrings(startline = 0, slenS = 1, slenE = 1):
    # Substrings must have length
    assert slenS > 0
    if slenS == slenE: slenS = 1 

    # Print first line and separator
    print(inhndle[startline], end='')
    print(Fore.WHITE + "=" * 60)
    for line in set(inhndle) - {inhndle[startline]}:
        


        
    

# print(Fore.RED + str(inhndle.readlines()))


#parser = argparse.ArgumentParser(description=\
#          'Automate Unity Testing from commandline')
#args = parser.parse_args()