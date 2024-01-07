#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("0")
    else:
        index = 1
        result = 0
        while index < argc:
            result += int(argv[index])
            index += 1
        print("{}".format(result))
