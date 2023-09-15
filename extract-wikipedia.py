# COMP7860 - Assignment 1
# Task 2: Gathering Data - Wikipedia
# Actor chosen: Sigourney Weaver

# In this script we extract the main text from the Wikipedia page for actor Tom Hanks ("Tom Hanks" in Wikipedia) and save it to the file "wikipedia.txt".

# Import necessary libraries.
import wikipedia
import re

# Define a list of actors. In this case it's only one.
Actors = ["Sigourney Weaver"]
words = []

# Create a loop to iterate through the list of actors and get their Wikipedia page.
for actor in Actors:
    page = wikipedia.page(actor)
    page_content = page.content

    # Split the text and exclude alphanumeric characters, using REs and count the words in the Wikipedia page.
    result = re.findall(r"[\w']+", page_content)
    counted = len(result)

    # Specify a file path for the output.
    file_path = "wikipedia.txt"

    # Print the word count for each actor. Here the result will only be one.
    print("There are " + str(counted) + " words in the {}  Wikipedia page.".format(actor))

    # Append the word count to the 'words' list.
    words.append(counted)

    # Open a file in write-mode and save the content.
    with open(file_path, "w", encoding="utf-8") as file:
         file.write(page_content)
