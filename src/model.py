import os
import json
import torch
import random
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from nltk.translate.chrf_score import sentence_chrf
from Levenshtein import distance as levenshtein_distance
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# from nltk.translate.bleu_score import sentence_bleu


# Load and Seed the Environment for Consistent Results
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


set_seed(41)


# Load the dataset
def load_dataset(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            data.append(json.loads(line))
    return data


dataset = load_dataset("data/code_completion_dataset.jsonl")

# Load model and tokenizer
checkpoint = "bigcode/tiny_starcoder_py"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

# Set the padding token if it's not defined
if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id


# Define the generation function
def generate_code_completion(model, tokenizer, prefix, middle, max_length=50):
    input_text = f"<fim_prefix>{prefix}<fim_middle>{middle}<fim_suffix>"
    inputs = tokenizer(input_text, return_tensors="pt", padding=True).to(device)

    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=len(inputs["input_ids"][0]) + max_length,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            temperature=0.6,  # Adjusted temperature for balanced randomness
            top_p=0.8,  # Top-p sampling for varied predictions
            do_sample=True,
            num_beams=5,  # Beam search for high-quality output
        )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    completion = generated_text[len(input_text) :].strip()
    return completion


# Generate predictions
for entry in dataset:
    entry["predicted_suffix"] = generate_code_completion(
        model, tokenizer, entry["prefix"], entry["middle"]
    )
    print(f"Function Name: {entry['function_name']}")
    print(f"Predicted Suffix: {entry['predicted_suffix']}\n")

# Save predictions in JSONL format
output_file_path = "data/code_completion_predictions.jsonl"
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
with open(output_file_path, "w") as output_file:
    for entry in dataset:
        json.dump(
            {
                "function_name": entry["function_name"],
                "prefix": entry["prefix"],
                "middle": entry["middle"],
                "actual_suffix": entry["suffix"],
                "predicted_suffix": entry["predicted_suffix"],
            },
            output_file,
        )
        output_file.write("\n")

print(f"Predictions saved to {output_file_path}")


# Evaluation functions
def evaluate_predictions(dataset):
    # ADDED
    chrf_scores = []
    bleu_scores = []
    levenshtein_distances = []

    smoothing_function = (
        SmoothingFunction().method1
    )  # Using method1 for basic smoothing

    for entry in dataset:
        actual_suffix = entry["suffix"].strip()
        predicted_suffix = entry["predicted_suffix"].strip()

        # chrF score
        chrf_scores.append(sentence_chrf(actual_suffix, predicted_suffix))

        # BLEU score with smoothing
        bleu_scores.append(
            sentence_bleu(
                [actual_suffix.split()],
                predicted_suffix.split(),
                smoothing_function=smoothing_function,
            )
        )

        # Levenshtein Distance
        levenshtein_distances.append(
            levenshtein_distance(actual_suffix, predicted_suffix)
        )

    # Aggregate results
    avg_chrf_score = np.mean(chrf_scores)
    avg_bleu_score = np.mean(bleu_scores)
    avg_levenshtein_distance = np.mean(levenshtein_distances)

    print(f"Average chrF Score: {avg_chrf_score:.4f}")
    print(f"Average BLEU Score with Smoothing: {avg_bleu_score:.4f}")
    print(f"Average Levenshtein Distance: {avg_levenshtein_distance:.2f}")
    # ADDED

    correct_predictions = sum(
        1
        for entry in dataset
        if entry["suffix"].strip() in entry["predicted_suffix"].strip()
    )
    accuracy = correct_predictions / len(dataset)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    # Calculate chrF score for each prediction as an additional metric
    chrf_scores = [
        sentence_chrf(entry["suffix"], entry["predicted_suffix"]) for entry in dataset
    ]
    avg_chrf_score = np.mean(chrf_scores)
    print(f"Average chrF score: {avg_chrf_score:.4f}")


evaluate_predictions(dataset)
