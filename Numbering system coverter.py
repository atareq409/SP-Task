# Abdallah Tarek Eid (20220482)
# Mohamed Abo-Obaida Mohamed Othman (20220727)
# Nour-Eleslam Mohamed Abdallah Mohamed (20231192)
 

#making functions to convert numbers and calling them after inserting the number from the user
def BinaryToDecimal(binary_number):
  decimal_number = 0
  binary_number = str(binary_number)[::-1]
  #to reverse the number
  for i in range(len(binary_number)):
        if binary_number[i] == '1':
            decimal_number += 2**i
  print ("Your number is : " , decimal_number)
  #this output will appear after the function is called


def DecimalToBinary(decimal_number):
    decimal_number = int(decimal_number)
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2
        
    print ("Your number is: " , binary_number)   


def BinaryToHexadecimal(binary_number):
    while len(binary_number) % 4 != 0:
        binary_number = '0' + binary_number
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    for i in range(0, len(binary_number), 4):
        four_bits = binary_number[i:i + 4]
        decimal_value = int(four_bits, 2)
        hexadecimal_digit = hex_digits[decimal_value]
        hexadecimal_number += hexadecimal_digit
    print ("Your number is: " , hexadecimal_number)


def HexadecimalToBinary(hexadecimal_number):
    hex_digits = "0123456789ABCDEF"
    binary_digits = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                     '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                     '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                     'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    hexadecimal_number = hexadecimal_number.upper()
    binary_number = ""
    for digit in hexadecimal_number:
        if digit in hex_digits:
            binary_number += binary_digits[digit]
    print ("Your number is: " , binary_number)


def DecimalToHexadecimal(decimal_number):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    decimal_number = int(decimal_number)
    if decimal_number == 0:
        print ("Your number is: " , "0")
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_digit = hex_digits[remainder]
        hexadecimal_number = hexadecimal_digit + hexadecimal_number
        decimal_number //= 16

    print ("Your number is: " , hexadecimal_number)


def HexadecimalToDecimal(hexadecimal_number):
    hex_digits = "0123456789ABCDEF"
    decimal_number = 0
    hexadecimal_number = hexadecimal_number.upper()    
    for digit in hexadecimal_number:
        if digit in hex_digits:
            decimal_number = decimal_number * 16 + hex_digits.index(digit)
    print ("Your number is: " , decimal_number)


def BinaryToOctal(binary_number):
    octal_digits = "01234567"
    octal_number = ""
    while len(binary_number) % 3 != 0:
        binary_number = '0' + binary_number
    for i in range(0, len(binary_number), 3):
        three_bits = binary_number[i:i + 3]
        decimal_value = int(three_bits, 2)
        octal_digit = octal_digits[decimal_value]
        octal_number += octal_digit
    print ("Your number is: " , octal_number)


def OctalToBinary(octal_number):
    binary_digits = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'}
    binary_number = ""
    for digit in octal_number:
        if digit in binary_digits:
            binary_number += binary_digits[digit]
    # this is for removing leading zeros
    binary_number = binary_number.lstrip('0')
    print ("Your number is: " , binary_number)


def DecimalToOctal(decimal_number):
    decimal_number = int(decimal_number)
    octal_digits = "01234567"
    octal_number = ""
    if decimal_number == 0:
        print ("Your number is: 0")
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_digit = octal_digits[remainder]
        octal_number = octal_digit + octal_number
        decimal_number //= 8
    print ("Your number is: " , octal_number)


def OctalToDecimal(octal_number):
    decimal_number = 0
    for digit in octal_number:
        if '0' <= digit <= '7':
            decimal_number = decimal_number * 8 + int(digit)
    print ("Your number is: " , decimal_number)


def HexadecimalToOctal(hexadecimal_number):
    hex_digits = "0123456789ABCDEF"
    octal_digits = "01234567"
    octal_number = ""
    hexadecimal_number = hexadecimal_number.upper()
    #  this is for padding the hexadecimal number with zeros to make its length a multiple of 3
    while len(hexadecimal_number) % 3 != 0:
        hexadecimal_number = '0' + hexadecimal_number
    for i in range(0, len(hexadecimal_number), 3):
        three_digits = hexadecimal_number[i:i + 3]
        decimal_value = int(three_digits, 16)
        # this converts the decimal value to octal
        octal_digit = ""
        while decimal_value > 0:
            remainder = decimal_value % 8
            octal_digit = octal_digits[remainder] + octal_digit
            decimal_value //= 8
        octal_number += octal_digit



def OctalToHexadecimal(octal_number):
    octal_digits = "01234567"
    hex_digits = "0123456789ABCDEF"
    hexadecimal_number = ""
    # to pad the octal number with zeros to make its length a multiple of 3
    while len(octal_number) % 3 != 0:
        octal_number = '0' + octal_number
    for i in range(0, len(octal_number), 3):
        three_digits = octal_number[i:i + 3]
        decimal_value = int(three_digits, 8)
        # This converts the decimal value to hexadecimal
        hexadecimal_digit = ""
        while decimal_value > 0:
            remainder = decimal_value % 16
            hexadecimal_digit = hex_digits[remainder] + hexadecimal_digit
            decimal_value //= 16
        
        hexadecimal_number += hexadecimal_digit

    print ("Your number is: " , hexadecimal_number)


def convertIt():
    Inserted_number = input("Insert the number: ")
    while True:
        print("Please select the base you want to convert a number from: ")
        print("A) Binary , B) Decimal , C) Hexadecimal , D) Octa")
        First_base = input("Enter your choice: ").upper()
        if First_base not in ["A", "B", "C", "D"]:        #Validation code
            print("Please select a valid choice")
        else:
            break

    while True:
        print("Please select the base you want to convert a number to: ")
        print("A) Binary , B) Decimal , C) Hexadecimal , D) Octa")
        second_base = input("Enter your choice: ").upper()
        if second_base not in ["A", "B", "C", "D"]:          #Validation code
            print("Please select a valid choice")
        else:
            break

    if First_base == "A" and second_base == "B":
        BinaryToDecimal(Inserted_number)              #-----------> calling functions
    elif First_base == "B" and second_base == "A":
        DecimalToBinary(Inserted_number)
    elif First_base == "A" and second_base == "C":
        BinaryToHexadecimal(Inserted_number)
    elif First_base == "C" and second_base == "A":
        HexadecimalToBinary(Inserted_number)
    elif First_base == "B" and second_base == "C":
        DecimalToHexadecimal(Inserted_number)
    elif First_base == "C" and second_base == "B":
        HexadecimalToDecimal(Inserted_number)
    elif First_base == "A" and second_base == "D":
        BinaryToOctal(Inserted_number)
    elif First_base == "D" and second_base == "A":
        OctalToBinary(Inserted_number)
    elif First_base == "B" and second_base == "D":
        DecimalToOctal(Inserted_number)
    elif First_base == "D" and second_base == "B":
        OctalToDecimal(Inserted_number)
    elif First_base == "C" and second_base == "D":
        HexadecimalToOctal(Inserted_number)
    elif First_base == "D" and second_base == "C":
        OctalToHexadecimal(Inserted_number)

def main():         
    print("╭── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ──╮")
    print("w 𝐓𝐨 𝐂𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫 𝐀𝐩𝐩")
    print("╰── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ──╯")
# 3ayz bonus bsraha :)
    while True:
        print("A) Insert a number \nB) exit the program")
        on_off = input("Enter your choice: ").upper()
        if on_off == "A":
            convertIt()
        elif on_off == "B":
            print("Goodbye!")
            break
        else:
            print("Please select a valid choice")


main()
