import os
import subprocess

comp_val = False

command = ""
executable = ""

def get_input():
    cmd = str(input(">>> "))
    return cmd.upper()

def get_file_paths():
    program = input("Program: ") + " "
    include = input("Flags Options: ")
    executable = input("Executable: ")

    if executable == "0":
        executable = " C:/Users/Acer/Downloads/C/EXECUTABLES/a.exe "
    if include == "0":
        with open("Flags.txt", "r") as f:
            include = f.read()

    include += " "
    executable += " "

    return program, include, executable

with open("VCPKG.txt", "r") as f:
            directory = f.readlines()

directory[0] = directory[0].replace("\n", "")
VCPKG = "gcc -I "+directory[0]+" -L "+directory[1]+" "

def build_command(program, include, executable):
    return VCPKG + program + include + "-o" + executable

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[1]
    output = process.decode('utf8').split('\n')
    return output

def print_output(output):
    for i in range(len(output)):
        print(output[i])

def execute_program(executable):
    process = subprocess.Popen(executable, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    output = process.decode('utf8').split('\n')
    print_output(output)

while True:
    cmd = get_input()

    if cmd in ["EDIT", "CRUN", "COMP", "COMPILE"]:
        program, include, executable = get_file_paths()
        command = build_command(program, include, executable)
        if cmd == "CRUN":
            output = execute_command(command)
            if output == [""]:
                execute_program(executable)
            else:
                print_output(output)
            comp_val = True
        elif cmd in ["COMP", "COMPILE"]:
            output = execute_command(command)
            comp_val = True
    elif cmd == "RUN":
        if comp_val:
            output = execute_command(command)
            if output == [""]:
                execute_program(executable)
            else:
                print_output(output)
        else:
            print("ERROR: No valid .exe file, try recompiling")
    elif cmd == "CLS":
        os.system("CLS")
    elif cmd == "EXIT":
        exit()
    elif cmd == "COMMAND":
        print(command)
    elif cmd in ["HELP", "?", "help?"]:
        print("""        GCC C/C++ COMPILER FOR VCPKG

        COMMANDS:
        cls = Clear the screen
        
        exit = Exits the application
        
        compile = Compiles the program
        
        run = Runs the compiled program
        
        edit = Edits the command used to compile or creates a
        new one, if you make flags prompt: "0",
        it will acces the Flags.txt, and make those your flags file
        if you make the compile directory prompt: "0",
        it will compile to the COMPILED folder.
        
        command = Prints the command used to compile
        
        crun = compiles & runs a program
        
        Any other command is answered by the windows command prompt.""")
    else:
        output = execute_command(cmd)
        print_output(output)