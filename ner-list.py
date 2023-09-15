# COMP7860 - Assignment 1 - Task 3: Identifying NERs.
# We write a script that extracts the NERs from the stanford-wikipedia.txt and stanford-fanwiki.txt files.
# The script takes words that have tags PERSON, ORGANIZATION or LOCATION, removes the tag and prints consecutive words
# that have the same tag. Once the tag changes, a new line is created with the new set of words.
# The output files are ner-list-wikipedia.txt and ner-list-fanwiki.txt, respectively.


# Import necessary modules.
import os

# Defne function that takes the input file, separates the words based on their tag and writes consecutive words with the same tag in one line.
def extract_consecutive_ners(input_filename, output_filename):
    # Open the input file.
    with open(input_filename, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8') as output_file:
        previous_ner = None           # variable to keep track of previous NER tag
        consecutive_ners = []         # empty list to store consecutive words with same NER tag

        # Loop to iterate over each line in the input file.
        for line in input_file:
            line = line.strip()
            if line:
                # Split the line by spaces.
                parts = line.split()
                for part in parts:
                    # Split each part by "/" to separate the word and NER tag.
                    word_ner = part.split('/')

                    # Check if there are exactly 2 elements (word and NER tag).
                    if len(word_ner) == 2:
                        word, ner = word_ner
                        # Only consider PERSON, ORGANIZATION, and LOCATION NERs.
                        if ner in ['PERSON', 'ORGANIZATION', 'LOCATION']:
                            if previous_ner == ner:
                                consecutive_ners.append(word)
                            else:
                                if consecutive_ners:
                                    # Write consecutive NERs to the output file.
                                    output_file.write(' '.join(consecutive_ners) + '\n')
                                    consecutive_ners = []
                                consecutive_ners.append(word)
                                previous_ner = ner
                        else:
                            if consecutive_ners:
                                # Write consecutive NERs to the output file
                                output_file.write(' '.join(consecutive_ners) + '\n')
                                consecutive_ners = []
                            previous_ner = None

        # Write the last consecutive NERs to the output file.
        if consecutive_ners:
            output_file.write(' '.join(consecutive_ners) + '\n')

# Process the wikipedia input file.
extract_consecutive_ners('stanford-wikipedia.txt', 'ner-list-wikipedia.txt')

# Process the fanwiki input file.
extract_consecutive_ners('stanford-fanwiki.txt', 'ner-list-fanwiki.txt')
