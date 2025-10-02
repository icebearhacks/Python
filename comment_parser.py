import sys
import re

def remove_comment_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip()
        if not stripped.startswith('#') and stripped.strip():
            cleaned_lines.append(line)
    with open(output_file, 'w') as f:
        f.writelines(cleaned_lines)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python parser.py <input.ps1> <output.ps1>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    remove_comment_lines(input_file, output_file)
    print(f"Cleaned script saved as {output_file}")
