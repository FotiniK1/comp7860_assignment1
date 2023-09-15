# COMP7860 - Assignment 1 - Task 2C: Stanford NER scripts.
# Here we have a script that applies the Stanford NEr system to downloaded texts. 
# In this case from Wikipedia (Sigourney Weaver) and Fandom (Jean Pierre Polnareff).

# Import "subprocess" module.
import subprocess

# Specify input and output file paths.
input_files = ["wikipedia.txt", "fanwiki.txt"]
output_files = ["stanford-wikipedia.txt", "stanford-fanwiki.txt"]

# Create empty output files.
for output_file in output_files:
    with open(output_file, "w", encoding="utf-8"):
        pass  # This creates an empty file.

# Loop through the input files and process them with Stanford NER. The results are saved in the corresponding output files.
for input_file, output_file in zip(input_files, output_files):
    try:
        process = subprocess.run(["./ner.sh", input_file], stdout=open(output_file, "w", encoding="utf-8"), stderr=subprocess.PIPE, check=True)
        print(f"Stanford NER processing completed for {input_file}. Results saved to {output_file}")

    # Capture any exceptions during the execution of subprocess.
    except subprocess.CalledProcessError as e:
        print(f"Error running Stanford NER script for {input_file}: {e}")


      # These last two lines are to print detailed error messages to find out where the problem lies.
      #  print("Error output:")
      #  print(e.stderr.decode('utf-8'))
