# GCC-VCPKG-compile-command-generator

I got bored of trying to make VCPKG work with VSCode so I decided to create my own program to compile my code.

To make the code run, you must first specify your VCPKG include directory in the fist line of the VCPKG.TXT file, and your VCPKG bin directory into the second line!

There are 3 main commands: compile, run, crun, and edit. 
Compile compiles the code, but first it needs to know where the program is. After it needs to be specified the flags for the compiler, 
however, if you do not want to have to specify them every time you open the program, you can write your flags into the first line of the 
Flags.txt file. In doing so, from now on, every time you open the program, if requested for flags, you can just type "0" and it will read the
file instead. A similar system is in place for the compile directory, if you simply type "0", it will automatically compile into the
COMPILE folder with the name a.exe.

Run, runs your code, once you have compiled.

Crun compiles and runs your code at the same time.

Edit allows you to edit your flags, .c program directory and compiled program directory. This is only necesary if you fucked up in the compile command.
