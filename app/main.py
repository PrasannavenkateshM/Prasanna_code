import sys

from basics.helloworld import hello_world
from basics.printstatements import printstatement
from patterns.lefthalfpyramid import lefthalfpyramid
from patterns.numberpyramid import numberpyramid
from patterns.righthalfpyramid import righthalfpyramid

def main():
    if len(sys.argv)<2:
        print("These are the programs available, please selct which one to run")
        return
    command =sys.argv[1]
    if command=="helloworld":
        hello_world()
    elif command=="printstatements":
        printstatement()
    elif command=="lefthalfpyramid":
        lefthalfpyramid()
    elif command=="numberpyramid":
        numberpyramid()
    elif command=="righthalfpyramid":
        righthalfpyramid()
if __name__=="__main__":
    main()