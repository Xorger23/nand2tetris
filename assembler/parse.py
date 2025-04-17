def parse(dest, comp, jump):
    destbin = ["0"] * 3
    jumpbin = ["0"] * 3
    if dest:
        for c in dest:
            if c == "M":
                destbin[2] = "1"
            elif c == "D":
                destbin[1] = "1"
            elif c == "A":
                destbin[0] = "1"

    if comp == "0":
        compbin = "1110101010"
    elif comp == "1":
        compbin = "1110111111"
    elif comp == "-1":
        compbin = "1110111010"
    elif comp == "D+1":
        compbin = "1110011111"
    elif comp == "A+1":
        compbin = "1110110111"
    elif comp == "M+1":
        compbin = "1111110111"
    elif comp == "D-1":
        compbin = "1110001110"
    elif comp == "A-1":
        compbin = "1110110010"
    elif comp == "M-1":
        compbin = "1111110010"
    elif comp == "D+A":
        compbin = "1110000010"
    elif comp == "D+M":
        compbin = "1111000010"
    elif comp == "D-A":
        compbin = "1110010011"
    elif comp == "D-M":
        compbin = "1111010011"
    elif comp == "A-D":
        compbin = "1110000111"
    elif comp == "M-D":
        compbin = "1111000111"
    elif comp == "D&A":
        compbin = "1110000000"
    elif comp == "D&M":
        compbin = "1111000000"
    elif comp == "D|A":
        compbin = "1110010101"
    elif comp == "D|M":
        compbin = "1111010101"
    elif comp == "D":
        compbin = "1110001100"
    elif comp == "A":
        compbin = "1110110000"
    elif comp == "M":
        compbin = "1111110000"
    elif comp == "!D":
        compbin = "1110001101"
    elif comp == "!A":
        compbin = "1110110001"
    elif comp == "!M":
        compbin = "1111110001"
    elif comp == "-D":
        compbin = "1110001111"
    elif comp == "-A":
        compbin = "1110110011"
    elif comp == "-M":
        compbin = "1111110011"
    else:
        compbin = "1110000000"

    if jump:
        nstat = False
        if jump[1] == "G":
            jumpbin[2] = "1"
        elif jump[1] == "L":
            jumpbin[0] = "1"
        elif nstat := (jump[1] == "N"):
            jumpbin[0] = "1"
            jumpbin[2] = "1"
        elif jump[1] == "M":
            jumpbin = ["1"] * 3
        if jump[1] == "E" or (jump[2] == "E" and not nstat):
            jumpbin[1] = "1"

    return compbin + "".join(destbin) + "".join(jumpbin)
