# Names: Sandya Devanahally and Vinayak Ranjan
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Assembler for circ file (reads the instructions.txt file and turns it into an img file)

# Program to convert assembly instructions from a file (instruction.txt) into hexadecimal output (image.txt)
# Function to convert a binary string into its numerical value
def bin_to_dec(binary_str):
    if binary_str == '':
        return 0
    return int(binary_str[0]) * (2 ** (len(binary_str) - 1)) + bin_to_dec(binary_str[1:])

# Function to convert a decimal number to binary with a specified number of bits
def dec_to_bin(decimal, num_bits=2):
    binary = bin(decimal)[2:]  # Convert to binary and remove the "0b" prefix
    if len(binary) > num_bits:  # Truncate if longer than num_bits
        return binary[-num_bits:]
    return binary.zfill(num_bits)  # Pad with leading zeros if shorter

# Open the input and output files
input_file = open("instruction.txt", "r")
output_file = open("image.txt", "w")
line_count = 0

# Process each line in the input file
for instruction_line in input_file:
    instruction = instruction_line.strip()  # Read and strip leading/trailing whitespace

    # Determine the control and instruction codes based on the operation
    if instruction[0:3] == "ADD":
        control_bits = "110100" if instruction[10:11] == "X" else "100100"
        operation_code = "0000"
    elif instruction[0:3] == "SUB":
        control_bits = "110100" if instruction[10:11] == "X" else "100100"
        operation_code = "0001"
    elif instruction[0:3] == "LDR":
        control_bits = "110001"
        operation_code = "0000"
    elif instruction[0:3] == "STR":
        control_bits = "001001"
        operation_code = "0000"
    elif instruction[0:3] == "MUL":
        control_bits = "110100" if instruction[10:11] == "X" else "100100"
        operation_code = "0010"
    else:
        continue  # Skip lines with unrecognized operations

    # Determine the destination register
    dest_reg = dec_to_bin(int(instruction[5:6]), num_bits=2)

    # Determine the first source register
    src_reg1 = dec_to_bin(int(instruction[8:9]), num_bits=2)

    # Determine the second source register or immediate value
    if instruction[10:11] == "X":
        src_reg2 = dec_to_bin(int(instruction[11:12]), num_bits=2)
    else:
        src_reg2 = dec_to_bin(int(instruction[10:11]), num_bits=2)

    # Combine the parts to form the opcode and enforce a 16-bit limit
    full_opcode = (control_bits + operation_code + src_reg2 + src_reg1 + dest_reg)[:16]

    # Convert the opcode to hexadecimal
    numeric_value = bin_to_dec(full_opcode)
    hex_value = hex(numeric_value)[2:].zfill(4)

    # Validate that the output is exactly 4 characters
    if len(hex_value) > 4:
        hex_value = hex_value[-4:]

    # Write the hexadecimal value to the output file
    output_file.write(hex_value + "\n")
    line_count += 1

# Close the input and output files
input_file.close()
output_file.close()

