#Init symbol table
#First pass to eval L-Commands
#Second pass to eval C- and A- commands
#USAGE: python main.py inputfile outputfile
from symboltable import SymbolTable
from parse import parse
from bit16 import bit16
from sys import argv
output = []
symbols = SymbolTable()
curpass = 0
num = -1
with open(argv[1], "r") as input_file:
    for line in input_file:
        line = line.strip()
        if line.startswith("//") or not line:
            pass
        elif line.startswith("("):
            symbols.add(line[1:-1], num + 1)
        else:
            num += 1
    input_file.seek(0)
    for num, line in enumerate(input_file):
        line = line.strip()
        if line.startswith("(") or line.startswith("//") or not line:
            pass
        elif line.startswith("@"):
            if line[1:].isdigit():
                output.append(bit16(int(line[1:])))
            else:
                output.append(bit16(symbols.add(line[1:], None)))
        else:
            parts = line.replace(";", "=").split("=")
            if len(parts) == 3:
                dest = parts[0]
                comp = parts[1]
                jump = parts[2]
            elif len(parts) == 2 and "=" in line:
                dest = parts[0]
                comp = parts[1]
                jump = None
            elif len(parts) == 2 and ";" in line:
                dest = None
                comp = parts[0]
                jump = parts[1]
            else:
                dest = None
                comp = parts[0]
                jump = None
            output.append(parse(dest, comp, jump))
with open(argv[1].replace(".asm", ".hack"), "w") as output_file:
    for o in output:
        output_file.write(o + "\n")
