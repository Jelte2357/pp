# usage: echo "input" | pp "character/string"; so its kind of like grep
import sys

if not sys.stdin.isatty():
    input = sys.stdin.read().strip()
    if len(sys.argv) != 2:
        print("Error: Wrong number of arguments, only 1 argument is allowed")
        exit()
    if len(input) == 0:
        print("Error: No input given")
        exit()
    else:
        if not sys.argv[1] in input:
            print("Error: Character(s) not found")
        else:
            print("\n".join(input.split(sys.argv[1])))
            
else:
    print("Error: No input given")
    exit()