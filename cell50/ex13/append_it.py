import sys

para = sys.argv[1:]
if len(para) == 0:
    print("none")
else:
    for param in para:
        if not param.endswith("ism"):
            print(f"{param}ism")