import argparse
import os
from colorama import Fore, Back, Style
from collections import Counter
from statistics import mean 
from math import floor

# Test for specific lengths or range of langths 
# test for entropy - does it change a lot? 
# Print firstline at the end to also color it 

inhndle = open('input.txt', 'r').readlines()

# Compare characters in each line at specific position
# i.e. in abc \n abc a is compared to a etc. 
def compareCharacterAtPosition(startline = 0):
    assert startline < len(inhndle)

    # Print first line and separator
    print(inhndle[startline], end='')
    print(Fore.WHITE + "=" * 60)
    for line in inhndle[ :startline] + inhndle[startline + 1:]:
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
def compareSubstrings(startline = 0, slenS = 1):
    # Substrings must have length
    assert slenS > 0

    # Print first line and separator
    print(inhndle[startline], end='')
    print(Fore.WHITE + "=" * 60)
    for line in inhndle[ :startline] + inhndle[startline + 1:]:
        linecopy = line[:]
        while linecopy:
            snip = linecopy[:slenS]
            linecopy = linecopy[slenS:]
            if snip in inhndle[startline]:
                print(Fore.GREEN + snip, end="")
            else:
                print(Fore.WHITE + snip, end="")
        print()
    
    print(Fore.WHITE + "=" * 60)
#        

def printEntropy(startline = 0):
    # enumerate elements in first line 
    for i, ps in enumerate(inhndle[startline]):
        # For each position, create list with all characters on this position (on other lines)
        charsAtPos = []
        for line in inhndle:
            # handle case when there is different number of elements in lists
            try:
                charsAtPos += line[i]
            except Exception:
                pass
        
        if not charsAtPos:
            continue

        avg = mean(list(dict(Counter(charsAtPos)).values()))
        print(":: ", avg)

        if avg < len(charsAtPos) / 6 or floor(avg) == 1:
            print(Fore.WHITE + ps, end="")
        elif avg < len(charsAtPos) / 5:
            print(Fore.GREEN + ps, end="")
        elif avg < len(charsAtPos) / 4:
            print(Fore.YELLOW + ps, end="")
        elif avg < len(charsAtPos) / 2:
            print(Fore.RED + ps, end="")
    print()

        
        
            
    

#compareSubstrings(slenS=2)
# printEntropy(0)
compareCharacterAtPosition(2)


#parser = argparse.ArgumentParser(description=\
#          'Automate Unity Testing from commandline')
#args = parser.parse_args()