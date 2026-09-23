import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        st = int(sys.argv[1])
        end = int(sys.argv[2])
        if st <= end:
            r = list(range(st, end + 1))
        else:
            r = list(range(st, end - 1, -1))
        print(r)
    except ValueError:
        print("none")