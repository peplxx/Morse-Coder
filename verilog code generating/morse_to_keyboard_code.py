from string import ascii_uppercase as ALPHABET

morze = {'A': '.-',
         'B': '-...',
         'C': '-.-.',
         'D': '-..',
         'E': '.',
         'F': '..-.',
         'G': '--.',
         'H': '....',
         'I': '..',
         'J': '.---',
         'K': '-.-',
         'L': '.-..',
         'M': '--',
         'N': '-.',
         'O': '---',
         'P': '.--.',
         'Q': '--.-',
         'R': '.-.',
         'S': '...',
         'T': '-',
         'U': '..-',
         'V': '...-',
         'W': '.--',
         'X': '-..-',
         'Y': '-.--',
         'Z': '--..',
         '1': '.----',
         '2': '..---',
         '3': '...--',
         '4': '....-',
         '5': '.....',
         '6': '-....',
         '7': '--...',
         '8': '---..',
         '9': '----.',
         '0': '-----'}

digit_code = {
    # HEX0  1  2  3  4  5  6  7
    1: [0, 1, 1, 0, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1, 0],
    3: [1, 1, 1, 1, 0, 0, 1, 0],
    4: [0, 1, 1, 0, 0, 1, 1, 0],
}

_ = '00000010'


def bin_morze(m):
    res = []
    m = ' ' * (4 - len(m)) + m
    for i, e in enumerate(m[::-1]):
        if e == ' ':
            res += [*(0, 0)]
        elif e == '-':
            res += [*(1, 1)]
        else:
            res += [*(1, 0)]
    return res


def sized(arr):
    return [f"1'b{(int(e)+1)%2}" for e in arr]


offset = 0
code = ['case (switches)']
print("KEYBOARD 1 RULES:")
for i in range(1, 5):
    for j in range(1, 5):
        letter = ALPHABET[offset]
        display1 = digit_code[i]
        display2 = digit_code[j]
        sds1 = [str(e) for e in display1]
        sds2 = [str(e) for e in display2]
        mletter = morze[letter]
        case = ''.join([str(e) for e in bin_morze(mletter)[::-1]])
        print(f"{mletter:>5} -> ", letter,f"{i}-{j}", f"ds1: {''.join(sds1)}", f"ds2: {''.join(sds2)}")

        code += [f"\t8'b{case}: begin \n "
                 f"\t\tds1 <= "+'{'+f"{', '.join(sized(sds1[::-1]))}"+'};\n'+" "
                 f"\t\tds2 <= "+'{'+f"{', '.join(sized(sds2[::-1]))}"+'};\n'+"\tend"]
        offset += 1

print("\n-------------------------------------------")
print("KEYBOARD 2 RULES:")
for i in range(1, 5):
    for j in range(1, 5):
        try:
            letter = ALPHABET[offset]
        except:
            break
        display1 = digit_code[i]
        display2 = digit_code[j].copy()
        display2[7] = 1
        sds1 = [str(e) for e in display1]
        sds2 = [str(e) for e in display2]
        mletter = morze[letter]
        case = ''.join([str(e) for e in bin_morze(mletter)[::-1]])
        print(f"{mletter:>5} -> ", letter,f"{i}-{j}.", f"ds1: {''.join(sds1)}", f"ds2: {''.join(sds2)}")

        code += [f"\t8'b{case}: begin \n "
                 f"\t\tds1 <= "+'{'+f"{', '.join(sized(sds1[::-1]))}"+'};\n'+" "
                 f"\t\tds2 <= "+'{'+f"{', '.join(sized(sds2[::-1]))}"+'};\n'+"\tend"]
        offset += 1

code += [f"\tdefault: begin \n "
         f"\t\tds1 <= "+'{'+f"{', '.join(sized(_[::-1]))}"+'};\n'+" "
         f"\t\tds2 <= "+'{'+f"{', '.join(sized(_[::-1]))}"+'};\n'+"\tend"]
code += ["endcase"]
print("\n-------------------------------------------\n"
      "GENERATED CODE:")
print(*code, sep='\n')
