import sys

para = sys.argv[1:]
if len(para) == 0:
    print("none")
else:
    print(f"parameters: {len(para)}")
    for param in para:
        print(f"{param}: {len(param)}")