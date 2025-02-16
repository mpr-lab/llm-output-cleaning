import os
import io 

file = "/Users/DaniJusto/Desktop/MPR Lab/sample_input_2.txt"

code_chunk_end = False
code_chunk = []
bracket_match = []
    
with open(file, 'r') as infile:
   
    line = infile.readline()

    # look for a line that has function name
    while not line.find("void saxpy(float *x, float *y, float a, int N)") != -1:
        line = infile.readline()

    # copy characters within the brackets
    while line and code_chunk_end == False:
        for char in line:
            if (char == '{'):
                code_chunk.append(char)
                bracket_match.append(char)
            else:
                if (char == '}'):
                    code_chunk.append(char)
                    bracket_match.pop()
                    if len(bracket_match) == 0:
                        code_chunk_end = True
                else:
                    code_chunk.append(char)

        line = infile.readline()

with open("/Users/DaniJusto/Desktop/MPR Lab/sample_cleaned.c", "w") as outfile:
    outfile.writelines(code_chunk)
