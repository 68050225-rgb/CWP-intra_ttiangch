import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    u_input = input("What was the parameter? ")
    
    if u_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")