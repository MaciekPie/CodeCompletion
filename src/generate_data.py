import os
import ast
import json


def split_code_to_lines(func_node, code_lines):
    start_line = func_node.lineno - 1
    end_line = func_node.end_lineno
    function_lines = code_lines[start_line:end_line]

    line_segments = []
    for i in range(1, len(function_lines)):
        prefix = "".join(function_lines[:i])
        target_line = function_lines[i]

        # In this setup, "middle" is empty, as we're focusing on line completions
        line_segments.append((prefix, "", target_line))

    return line_segments


def process_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)
    code_lines = code.splitlines(keepends=True)
    dataset = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            line_segments = split_code_to_lines(node, code_lines)

            for prefix, middle, suffix in line_segments:
                entry = {
                    "function_name": func_name,
                    "prefix": prefix,
                    "middle": middle,
                    "suffix": suffix,
                }
                dataset.append(entry)

    return dataset


def save_dataset(dataset, output_file):
    with open(output_file, "w") as file:
        for entry in dataset:
            json.dump(entry, file)
            file.write("\n")


def main(input_folder, output_file):
    all_data = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_data = process_file(file_path)
                all_data.extend(file_data)

    save_dataset(all_data, output_file)
    print(f"Dataset saved to {output_file}")


if __name__ == "__main__":
    input_folder = "src/examples"
    output_file = "data/code_completion_dataset.jsonl"
    main(input_folder, output_file)
