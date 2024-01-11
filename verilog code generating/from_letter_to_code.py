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

def generate_bin(r, c):
    row = list('0000')
    row[r] = '1'
    row = ''.join(row)
    col = list('0000')
    col[c] = '1'
    col = ''.join(col)
    return row + col


def generate_light_code(m: str):
    ans = {
        True: [1] * 4,
        False: [1] * 4
    }
    pointer = 0
    d = True
    mpointer = 0
    m = m[::-1]
    while mpointer < len(m):
        symbol = m[mpointer]
        if (symbol == '.') == d:
            ans[d][pointer] = 0
            mpointer += 1
        d = not (d)
        if d: pointer += 1
    code = [*ans[False][::-1]] + [*ans[True][::-1]]
    code = [f"1'b{e}" for e in code]
    return code


alpha_ofset = 0
alpha_end = False
for i in range(4):
    for j in range(4):
        index = i * 4 + j
        c = chr(ord('A') + index + alpha_ofset)
        binindex = generate_bin(i, j)
        code = generate_light_code(morze[c])
        if c == 'Z':
            alpha_end = True
            break
        print(f"8'b{binindex}: out <= " + '{' + ', '.join(code) + '}' + f'; // {c}  {morze[c]}')
    if alpha_end:
        break
print("default    : out <= {1'b1, 1'b1, 1'b1, 1'b1, 1'b1, 1'b1, 1'b1, 1'b1}; // all lights turned off")
