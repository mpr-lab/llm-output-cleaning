input_file = "/Users/nargizakhmetova/Documents/VS Cd/MRP Lab/test1.txt"
output_file = "/Users/nargizakhmetova/Documents/VS Cd/MRP Lab/empty.txt"

signature = "float sum(float *X, int N)"

with open(input_file, 'r') as f:
    content = f.read()

sig_index = content.find(signature)
if sig_index == -1:
    raise ValueError("Function signature not found in the file.")

start_brace = content.find("{", sig_index)
if start_brace == -1:
    raise ValueError("Opening brace '{' not found after the function signature.")

brace_count = 0
end_index = None
for i in range(start_brace, len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end_index = i + 1  
            break

if end_index is None:
    raise ValueError("Could not find a matching closing brace '}'.")

function_code = content[sig_index:end_index]

with open(output_file, 'w') as f:
    f.write(function_code)
