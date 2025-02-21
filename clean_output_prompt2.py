import os
import io 

# Directory where the prompt files are stored
for i in range(1,101):
    input_dir = f"pass-k{i}-poly-coder"
    output_dir = f"pass-k{i}-poly-coder/cleaned/"
    os.makedirs(output_dir, exist_ok=True)

#file to process
    file = "prompt_2.c"
            
    input_path = os.path.join(input_dir, file)
    output_path = os.path.join(output_dir, file)

    code_chunk_end = False
    code_chunk = []
    bracket_match = []

    try:   
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

    # Save the cleaned code to a new file
        with open(output_path, "w") as outfile:
            outfile.writelines(code_chunk)

        print(f"Processed and saved: {output_path}")

    except Exception as e:
        print(f"Failed to process {file}: {e}")

print("All files processed successfully!")
