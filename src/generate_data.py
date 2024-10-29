import ast
import os
import json


def split_function_code(func_node, code_lines):
    """
    Splits a function into prefix, middle, and suffix.
    """
    # Get the start and end lines of the function (1-based indexing in AST)
    start_line = func_node.lineno - 1  # adjust to 0-based
    end_line = func_node.end_lineno

    # Extract function lines
    function_lines = code_lines[start_line:end_line]

    # Prefix: up to function header (first line)
    prefix = function_lines[0]

    # Middle: placeholder for completion
    middle = "# Code completion starts here\n"

    # Suffix: everything after the function header
    suffix = "".join(function_lines[1:])

    return prefix, middle, suffix


def process_file(file_path):
    """
    Processes a Python file, splits each function, and returns dataset entries.
    """
    with open(file_path, "r") as file:
        code = file.read()

    # Parse code and get AST
    tree = ast.parse(code)
    code_lines = code.splitlines(keepends=True)

    dataset = []

    # Traverse the AST to find function definitions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            prefix, middle, suffix = split_function_code(node, code_lines)

            # Create the dataset entry
            entry = {
                "function_name": func_name,
                "prefix": prefix,
                "middle": middle,
                "suffix": suffix,
            }
            dataset.append(entry)

    return dataset


def save_dataset(dataset, output_file):
    """
    Saves the dataset to a JSONL (JSON Lines) file.
    """
    with open(output_file, "w") as file:
        for entry in dataset:
            json.dump(entry, file)
            file.write("\n")  # Newline for JSONL format


def main(input_folder, output_file):
    """
    Main function to process all Python files in a folder.
    """
    all_data = []

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_data = process_file(file_path)
                all_data.extend(file_data)

    # Save all processed functions to the output file
    save_dataset(all_data, output_file)
    print(f"Dataset saved to {output_file}")


# Specify input folder and output file
if __name__ == "__main__":
    input_folder = "src\\examples"
    output_file = "data/code_completion_dataset.jsonl"
    main(input_folder, output_file)
