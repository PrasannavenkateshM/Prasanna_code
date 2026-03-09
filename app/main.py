import sys

from basics.helloworld import hello_world

def main():
    if len(sys.argv)<2:
        print("These are the programs available, please selct which one to run")
        return
    command =sys.argv[1]
    if command=="helloworld":
        hello_world()
if __name__=="__main__":
    main()