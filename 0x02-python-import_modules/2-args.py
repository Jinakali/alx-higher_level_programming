#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[1]))
    else:
        print("{} arguments:".format(argc))
        index = 1
        while index <= argc:
            print("{}: {}".format(index, argv[index]))
            index += 1
