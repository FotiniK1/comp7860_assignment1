# COMP7860 - Assignment 1 -  Task 5: Fixing NERs.
# We write a script that changes the tags of punctuation marks to always be '/O'.
# The script is run on the wikipedia.txt and fanwiki.txt files and gives outputs fixed-wikipedia.txt and fixed-fanwiki.txt, respectively.

# Import necessary modules.
import subprocess
import os

# Function to run Stanford NER and tag punctuation marks with /O.
def run_stanford_ner(input_file, output_file):
    try:
        # Run Stanford NER on the input file.
        process = subprocess.run(["./ner.sh", input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        stdout = process.stdout.decode("utf-8")

        # Post-process the output to tag punctuation with /O.
        modified_output = tag_punctuation_with_O(stdout)

        with open(output_file, "w", encoding="utf-8") as output_file:
            output_file.write(modified_output)

        print(f"Stanford NER processing completed for {input_file}. Results saved to {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error running Stanford NER script for {input_file}: {e}")

# Function to tag punctuation with /O.
def tag_punctuation_with_O(text):       # Takes output text from  Stanford NER as input.
    lines = text.split("\n")            # Splits the text into lines and processes each line.
    tagged_lines = []

    for line in lines:
        parts = line.split("\t")        # Each line is split into the two word-tag parts.
        if len(parts) == 2:
            word, tag = parts
            if any(char in word for char in '.,!?;:"\'()'):         # Checks if a word contains punctuation characters.
                tag = '/O'                                          # Changes the tag to '/O'.
            tagged_lines.append(f"{word}\t{tag}")                   # Appends the modified line to a list.
        else:
            tagged_lines.append(line)

    return "\n".join(tagged_lines)               # Joins the lines form the list and returns the modified text.

# Specify input and output file paths.
input_files = ["wikipedia.txt", "fanwiki.txt"]
output_files = ["fixed-wikipedia.txt", "fixed-fanwiki.txt"]

# Create empty output files.
for output_file in output_files:
    with open(output_file, "w", encoding="utf-8"):
        pass  # This creates an empty file.

# Loop through the input files and process them with Stanford NER.
for input_file, output_file in zip(input_files, output_files):
    run_stanford_ner(input_file, output_file)
