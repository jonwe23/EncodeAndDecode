# Program 2 (Decode) - decode binary to text


input_file = open("findcode_output.txt")  # opens binary output file from program 1
output_file = open("decode_output.txt", "w")  # opens new file
binary_string = input_file.read()  # reads file
bstring_list = binary_string.split(".")
binary_string = bstring_list[1]


# converting binary to string
def decode(x: str):
    ans = ""  # empty string that will hold converted binary to text
    while len(x) > 4:  # while loop that makes sure length of each binary number is greater than 4
        if x[0] == "0":  # checks if binary value is long or short bit
            if x[:7] == "0000001":  # checks first 7 values
                ans += "b"  # adds b to empty string
                x = x[7::]  # replaces that binary value with ""
            elif x[:7] == "0000011":
                ans += "c"
                x = x[7::]
            elif x[:7] == "0010111":
                ans += "d"
                x = x[7::]
            elif x[:7] == "0001111":
                ans += "f"
                x = x[7::]
            elif x[:7] == "0011111":
                ans += "g"
                x = x[7::]
            elif x[:7] == "0111111":
                ans += "h"
                x = x[7::]
            elif x[:7] == "0000010":
                ans += "j"
                x = x[7::]
            elif x[:7] == "0000100":
                ans += "k"
                x = x[7::]
            elif x[:7] == "0001000":
                ans += "l"
                x = x[7::]
            elif x[:7] == "0010000":
                ans += "m"
                x = x[7::]
            elif x[:7] == "0100000":
                ans += "n"
                x = x[7::]
            elif x[:7] == "0000101":
                ans += "p"
                x = x[7::]
            elif x[:7] == "0001010":
                ans += "q"
                x = x[7::]
            elif x[:7] == "0010101":
                ans += "r"
                x = x[7::]
            elif x[:7] == "0101011":
                ans += "s"
                x = x[7::]
            elif x[:7] == "0000110":
                ans += "t"
                x = x[7::]
            elif x[:7] == "0001100":
                ans += "v"
                x = x[7::]
            elif x[:7] == "0011000":
                ans += "w"
                x = x[7::]
            elif x[:7] == "0110000":
                ans += "z"
                x = x[7::]
            elif x[:7] == "0000111":
                ans += "x"
                x = x[7::]
            elif x[:7] == "0001110":
                ans += "B"
                x = x[7::]
            elif x[:7] == "0011100":
                ans += "C"
                x = x[7::]
            elif x[:7] == "0111000":
                ans += "D"
                x = x[7::]
            elif x[:7] == "0001101":
                ans += "F"
                x = x[7::]
            elif x[:7] == "0011011":
                ans += "G"
                x = x[7::]
            elif x[:7] == "0110111":
                ans += "H"
                x = x[7::]
            elif x[:7] == "0001001":
                ans += "J"
                x = x[7::]
            elif x[:7] == "0010010":
                ans += "K"
                x = x[7::]
            elif x[:7] == "0100100":
                ans += "L"
                x = x[7::]
            elif x[:7] == "0011101":
                ans += "M"
                x = x[7::]
            elif x[:7] == "0111101":
                ans += "N"
                x = x[7::]
            elif x[:7] == "0110101":
                ans += "P"
                x = x[7::]
            elif x[:7] == "0111010":
                ans += "Q"
                x = x[7::]
            elif x[:7] == "0101100":
                ans += "R"
                x = x[7::]
            elif x[:7] == "0001011":
                ans += "S"
                x = x[7::]
            elif x[:7] == "0111110":
                ans += "T"
                x = x[7::]
            elif x[:7] == "0100111":
                ans += "V"
                x = x[7::]
            elif x[:7] == "0100010":
                ans += "W"
                x = x[7::]
            elif x[:7] == "0101000":
                ans += "Z"
                x = x[7::]
            elif x[:7] == "0010100":
                ans += "X"
                x = x[7::]
            elif x[:7] == "0110100":
                ans += "\n"
                x = x[7::]
            elif x[:7] == "0110011":
                ans += ","
                x = x[7::]
            elif x[:7] == "0111001":
                ans += "!"
                x = x[7::]
            elif x[:7] == "0010011":
                ans += "'"
                x = x[7::]
            elif x[:7] == "0100101":
                ans += '"'
                x = x[7::]
        elif x[0] == "1":  # checks if binary value is long or short bit
            if x[:5] == "11011":  # checks first 5 values
                ans += "a"  # adds a to empty string
                x = x[5::]  # replaces that binary value with ""
            elif x[:5] == "10010":
                ans += "e"
                x = x[5::]
            elif x[:5] == "11111":
                ans += "i"
                x = x[5::]
            elif x[:5] == "10100":
                ans += "o"
                x = x[5::]
            elif x[:5] == "11001":
                ans += "u"
                x = x[5::]
            elif x[:5] == "10000":
                ans += "y"
                x = x[5::]
            elif x[:5] == "11101":
                ans += "A"
                x = x[5::]
            elif x[:5] == "11000":
                ans += "E"
                x = x[5::]
            elif x[:5] == "11010":
                ans += "I"
                x = x[5::]
            elif x[:5] == "10011":
                ans += "O"
                x = x[5::]
            elif x[:5] == "11110":
                ans += "U"
                x = x[5::]
            elif x[:5] == "10001":
                ans += "Y"
                x = x[5::]
            elif x[:5] == "10110":
                ans += " "
                x = x[5::]
            elif x[:5] == "10111":
                ans += "."
                x = x[5::]
    return ans  # returns completed string


text_output = decode(binary_string)
output_file.write(text_output)  # writes code into file
output_file.close()  # closes file