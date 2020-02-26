import sys
import subprocess

# usage: javacr file_path.java [args]
def main():
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        args = sys.argv[2:]
        j = Javacr(file, args)
        j.compile()
        j.run()
    else:
        print(bcolored(bcolors.OKBLUE, "usage: javacr file_path.java [args]"))


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def bcolored(mode, text):
        return mode + text + bcolors.ENDC

class Javacr:
    def __init__(self, file, args):
        self.file = file
        self.args = args
        self.err = False

    def compile(self):
        print(bcolored(bcolors.OKGREEN, "\tmode: compile java file"))
        print(bcolored(bcolors.OKGREEN, f"\trun command: {bcolors.BOLD} javac -g {self.file}"))
        
        process = subprocess.run(["javac", "-g", self.file], shell= True, capture_output= True)
        if (process.stderr != b''):
            self.err = True
            print(bcolored(bcolors.FAIL, "\tfail found, details:"))
            print(bcolored(bcolors.BOLD, process.stderr.decode('ascii')))
        else:
            print(bcolored(bcolors.WARNING, "\t\t.::COMPILE SUCCESS::."))            
    
    def run(self):
        print(bcolored(bcolors.OKGREEN, "\tmode: run java file"))
        if not self.err:
            command = f"java {self.file.split('.')[0]}"
            for i in self.args: command += i
            print(bcolored(bcolors.OKGREEN, f"\trun command: {bcolors.BOLD} {command}"))
            print(bcolored(bcolors.WARNING, "\t\t.::EXECUTION::. "))
            process = subprocess.run(["java", self.file.split(".")[0]], shell= True)
        else:
            print(bcolored(bcolors.FAIL, "\trun java file aborted"))

if __name__ == "__main__":
    main()