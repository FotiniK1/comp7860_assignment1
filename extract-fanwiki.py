# COMP7860 - Assignment 1
# Task 2: Gathering Data - Fandom
# Character chosen: Jean Pierre Polnareff

# In this script we extract the main text from the fandom.com page for the character Jean Pierre Polnareff from 
# Jojo's Bizarre Adventure.

# Import the necessary modules.
import fandom
import re

# Set the wiki to the Jojo anime in fandom.com.
fandom.set_wiki("Jojo")

# Search for the precise name of the character and limit the results to 1 (the first that comes up).
character_search_result = fandom.search("Jean Pierre Polnareff", results=1)

# Check if there are results for the character.
if character_search_result:

    # Retrieve character information.
    character = character_search_result[0]
    character_name = character[0]

    # Initialise empty list.
    words = []

    # Fetch the character page.
    page = fandom.page(character_name)

    # Concatenate the content of different sections into a single variable ('text').
    text = " "
    for content in page.content["sections"]:
        text += content["content"]

    # Regular expressions to split the text and exclude alphanumeric characters.
    # The words are counted and the word-count is stored in 'counted'.
    result = re.findall(r"[\w']+", text)
    counted = len(result)

    # Specify a file path where the content is saved.
    file_path = "fanwiki.txt"

    # Print the word-count and character's name.
    print("There are " + str(counted) + " words in the {} Fandom page.".format(character_name))

    # Append word-count to the list 'words'.
    words.append(counted)

    # Open the output file in write-mode and save the content.
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

# Print the below sentense, if the character is not found.
else:
    print("Character not found in the search results.")
