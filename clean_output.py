import os 
import io 
import re
#clean file by keeping only one MPI average
def clean_output(input_path,output_path):
    try: 
        if not os.path.exist (input_path):
            print(f"Input file not found: {input_path}")
            return
        with open(input_path, "r") as infile:
            generated_output = infile.read()
        function_pattern = r"/\*\s*Use MPI to compute the average of X across ranks.*?\*/\s*double mpiAverage\(double X\)\s*{.*?return sum / size;\s*}"
        functions = re.findall(function_pattern, generated_output, re.DOTALL)

        cleaned_content = generated_output.replace(functions[0], "", functions.count(functions[0]) - 1)
        cleaned_content = functions[0] + cleaned_content.replace(functions[0], "", functions.count(functions[0]))
        with open(output_path, "w") as outfile:
            outfile.write(cleaned_content)
        print(f"Processed and saved: {output_path}")

    except Exception as e:
        print(f"Failed to process {input_path}: {e}")
for i in range(1, 101):
    input_dir = f"pass-k{i}-meta-llama"
    output_dir = os.path.join(input_dir, "cleaned")
    os.makedirs(output_dir, exist_ok=True)

input_path = os.path.join(input_dir, "prompt_3.c")
output_path = os.path.join(output_dir, "prompt_3.c")
clean_output(input_path, output_path)


