input_file = open("text_input.txt") # opens text file
file_string = input_file.read() # reads the file
output_file = open("findcode_output.txt", "w") # opens new file to put converted text into

def findcode(x: str):
    ans = "" # empty string that will hold converted text to binary
    for i in x: # checks each letter in the string x
       if i == "a":
           ans += "11011" # binary value of a - adds binary value to the new string
       elif i == "b":
           ans += "0000001" # binary value of b - adds binary value to the new string
       elif i == "c":
           ans += "0000011" # binary value of c - adds binary value to the new string
       elif i == "d":
            ans += "0010111" # binary value of d - adds binary value to the new string
       elif i == "e":
           ans += "10010" # binary value of e - adds binary value to the new string
       elif i == "f":
           ans += "0001111" # binary value of f - adds binary value to the new string
       elif i == "g":
           ans += "0011111" # binary value of g - adds binary value to the new string
       elif i == "h":
           ans += "0111111" # binary value of h - adds binary value to the new string
       elif i == "i":
           ans += "11111" # binary value of i - adds binary value to the new string
       elif i == "j":
           ans += "0000010" # binary value of j - adds binary value to the new string
       elif i == "k":
           ans += "0000100" # binary value of k - adds binary value to the new string
       elif i == "l":
           ans += "0001000" # binary value of l - adds binary value to the new string
       elif i == "m":
           ans += "0010000" # binary value of m - adds binary value to the new string
       elif i == "n":
           ans += "0100000" # binary value of n - adds binary value to the new string
       elif i == "o":
           ans += "10100" # binary value of o - adds binary value to the new string
       elif i == "p":
           ans += "0000101" # binary value of p - adds binary value to the new string
       elif i == "q":
           ans += "0001010" # binary value of q - adds binary value to the new string
       elif i == "r":
           ans += "0010101" # binary value of r - adds binary value to the new string
       elif i == "s":
           ans += "0101011" # binary value of s - adds binary value to the new string
       elif i == "t":
           ans += "0000110" # binary value of t - adds binary value to the new string
       elif i == "u":
           ans += "11001" # binary value of u - adds binary value to the new string
       elif i == "v":
           ans += "0001100" # binary value of v - adds binary value to the new string
       elif i == "w":
           ans += "0011000" # binary value of w - adds binary value to the new string
       elif i == "y":
           ans += "10000" # binary value of y - adds binary value to the new string
       elif i == "z":
           ans += "0110000" # binary value of z - adds binary value to the new string
       elif i == "x":
           ans += "0000111" # binary value of x - adds binary value to the new string
       elif i == "A":
           ans += "11101" # binary value of A - adds binary value to the new string
       elif i == "B":
           ans += "0001110" # binary value of B - adds binary value to the new string
       elif i == "C":
           ans += "0011100" # binary value of C - adds binary value to the new string
       elif i == "D":
           ans += "0111000" # binary value of D - adds binary value to the new string
       elif i == "E":
           ans += "11000" # binary value of E - adds binary value to the new string
       elif i == "F":
           ans += "0001101" # binary value of F - adds binary value to the new string
       elif i == "G":
           ans += "0011011" # binary value of G - adds binary value to the new string
       elif i == "H":
           ans += "0110111" # binary value of H - adds binary value to the new string
       elif i == "I":
           ans += "11010" # binary value of I - adds binary value to the new string
       elif i == "J":
           ans += "0001001" # binary value of J - adds binary value to the new string
       elif i == "K":
           ans += "0010010" # binary value of K - adds binary value to the new string
       elif i == "L":
           ans += "0100100" # binary value of L - adds binary value to the new string
       elif i == "M":
           ans += "0011101" # binary value of M - adds binary value to the new string
       elif i == "N":
           ans += "0111101" # binary value of N - adds binary value to the new string
       elif i == "O":
           ans += "10011" # binary value of O - adds binary value to the new string
       elif i == "P":
           ans += "0110101" # binary value of P - adds binary value to the new string
       elif i == "Q":
           ans += "0111010" # binary value of Q - adds binary value to the new string
       elif i == "R":
           ans += "0101100" # binary value of R - adds binary value to the new string
       elif i == "S":
           ans += "0001011" # binary value of S - adds binary value to the new string
       elif i == "T":
           ans += "0111110" # binary value of T - adds binary value to the new string
       elif i == "U":
           ans += "11110" # binary value of U - adds binary value to the new string
       elif i == "V":
           ans += "0100111" # binary value of V - adds binary value to the new string
       elif i == "W":
           ans += "0100010" # binary value of W - adds binary value to the new string
       elif i == "Y":
           ans += "10001" # binary value of Y - adds binary value to the new string
       elif i == "Z":
           ans += "0101000" # binary value of Z - adds binary value to the new string
       elif i == "X":
           ans += "0010100" # binary value of X - adds binary value to the new string
       elif i == "\n":
           ans += "0110100" # binary value of \n - adds binary value to the new string
       elif i == " ":
           ans += "10110" # binary value of space - adds binary value to the new string
       elif i == ".":
           ans += "10111" # binary value of . - adds binary value to the new string
       elif i == ",":
           ans += "0110011" # binary value of , - adds binary value to the new string
       elif i == "!":
           ans += "0111001" # binary value of ! - adds binary value to the new string
       elif i == "'":
           ans += "0010011" # binary value of ' - adds binary value to the new string
       elif i == '"':
           ans += "0100101" # binary value of " - adds binary value to the new string
    y = ans.count("1") + ans.count("0") # counts how many binary numbers
    y = str(y) # changes int to string
    ans = y + "." + ans # adds total of binary numbers and period
    return ans
binary = findcode(file_string) # inputs function into file
output_file.write(binary) # writes in converted text into file
output_file.close() # closes file