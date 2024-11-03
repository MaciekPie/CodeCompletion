import json

# Load predictions
with open("data/code_completion_predictions.jsonl", "r") as file:
    predictions = [json.loads(line) for line in file]


# Define a labeling function
def label_predictions(predictions):
    labeled_data = []
    for entry in predictions:
        actual = entry["actual_suffix"].strip()
        predicted = entry["predicted_suffix"].strip()

        print(f"Function Name: {entry['function_name']}")
        print(f"Prefix: {entry['prefix']}")
        print(f"Actual Suffix: {actual}")
        print(f"Predicted Suffix: {predicted}\n")

        # Prompt for manual labeling
        print("Label the prediction quality:")
        print("1 - Exact Match\n2 - Close Match\n3 - Mismatch")

        label = input("Enter label (1, 2, or 3): ")

        # Map input to labels
        if label == "1":
            label_text = "Exact Match"
        elif label == "2":
            label_text = "Close Match"
        else:
            label_text = "Mismatch"

        # Append labeled entry
        labeled_entry = {
            "function_name": entry["function_name"],
            "prefix": entry["prefix"],
            "actual_suffix": actual,
            "predicted_suffix": predicted,
            "label": label_text,
        }
        labeled_data.append(labeled_entry)
        print("\n" + "-" * 40 + "\n")

    return labeled_data


# Run labeling
labeled_data = label_predictions(predictions)

# Save labeled data
with open("data/labeled_code_completion_predictions.jsonl", "w") as file:
    for entry in labeled_data:
        json.dump(entry, file)
        file.write("\n")

print("Labeled data saved to data/labeled_code_completion_predictions.jsonl")
