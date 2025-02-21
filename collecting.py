import os 

for i in range(1, 101):
    input_dir = f"pass-k{i}-meta-llama"
    output_dir = f"pass-k{i}-meta-llama/cleaned/"
    
    os.markedir(output_dir, exist_ok = True)

    files = ["prompt_1.c", "prompt_2.c", "prompt_3.c",]

    for file in files: 
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)


        try:
            with open(input_path, "r") as infile: 
                lines = infile.readlines()
                inside_code_block = False
                first_code_block = []

                for line in lines: 
                    if line.strip() == "XXXXXX":
                        inside_code_block = True
                        continue

                    if inside_code_block and line.strip() == "XXXXX":
                        break

                    if inside_code_block:
                        first_code_block.append(line)

            with open(output_path, "w") as outfile:
                outfile.writelines(first_code_block)

            print(f"Processed and saved: {output_path}")

        except Exception as e: 
            print(f"Failed to process {file} because {e}")

    print("All files processed successfully")    