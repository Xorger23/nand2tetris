#Init symbol table
#First pass to eval L-Commands
#Second pass to eval C- and A- commands
#USAGE: python main.py inputfile outputfile
from symboltable import SymbolTable
from parse import parse
from sys import argv
output = []
symbols = SymbolTable()
curpass = 0
with open(argv[1], "r") as input_file:
    if curpass == 0:
        for num, line in enumerate(input_file):
            line = line.strip()
            if line.startswith("("):
                output.append(''.join( c for c in bin(symbols.add(line[1:-1], num + 1)) if  c != "b" ))
        curpass += 1
    else:
        for num, line in enumerate(input_file):
            line = line.strip()
            if line.startswith("(") or line.startswith("//"):
                pass
            elif line.startswith("@"):
                if line[1:].isdigit():
                    output.append(''.join( c for c in bin(int(line[1:])) if  c != "b" ))
                symbols.add(line[1:], None)
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
