# COMP7860 - Assignment 1 - Task 4A: Making tag corrections.
# The first part of this task is to create a "gold standard" annotated version of our wikipedia and fanwiki texts.
# The NER tagger was applied to the wikipedia.txt and fanwiki.txt files in the "Gathering Data" task, producing
# the stanford-wikipedia.txt and stanford-fanwiki.txt files, respectively. To create the gold standard files, I copied
# the text from each of the latter files and corrected the wrong tags as well as words that had not been separated properly.
# The corrected files were named: standard-wikipedia-corr.txt and standard-fanwiki-corr.txt.



# COMP7860 - Assignment 1 - Task 4B: Changing the "gold standard" files into the correct format.
# The script below takes the corrected files, splits the words from the tags and writes each word-tag pair
# in a line, separated by a tab-space.


# Define input and output file names.
input_files = ["stanford-wikipedia-corr.txt", "stanford-fanwiki-corr.txt"]
output_files = ["wikipedia-gold.txt", "fanwiki-gold.txt"]

# Process each input file.
for i in range(len(input_files)):
    with open(input_files[i], 'r', encoding='utf-8') as infile:          # Open each input file.
        data = infile.read().split()        # Read and split the input data by whitespace.

    # Initialize lists to store words and tags.
    words = []
    tags = []

    # Process each data entry (word-tag pairs).
    for entry in data:
        parts = entry.split('/')        # Split each entry by '/'.
        if len(parts) == 2:             # Check that 'parts' contains 2 elements.
            word, tag = parts           # If so, extract the elements.
            words.append(word)          # Add 'word' component in 'words' list.
            tags.append(tag)            # Add 'tag' component in 'tags' list.

    # Write the processed data to the output file.
    with open(output_files[i], 'w', encoding='utf-8') as outfile:      # Open the output files.
        for word, tag in zip(words, tags):             # Iterate through the 'words' and 'tags' lists and pair each word with corresponding tag.
            outfile.write(f"{word}\t{tag}\n")          # Write word and tag separated by a tab and followed by a newline.
